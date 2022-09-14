use std::cmp::{max, min};
use std::collections::{HashMap, HashSet};
use std::sync::mpsc::channel;
use std::time::Duration;

use itertools::Itertools;
use petgraph::prelude::DiGraph;
use petgraph::stable_graph::IndexType;
use petgraph::visit::IntoNeighborsDirected;
use petgraph::{Directed, Direction};
use petgraph::{Graph, Undirected};
use rand::distributions::Bernoulli;
use rand::prelude::*;
use rand::thread_rng;
use running_average::RealTimeRunningAverage;
use threadpool::ThreadPool;

fn calc_total_pointers(graph: &Graph<usize, (), Directed>) -> usize {
    let mut count = 0;
    for node in graph.node_indices() {
        for _neighbor in graph.neighbors_directed(node, Direction::Outgoing) {
            count += 1;
        }
    }
    count
}

fn calc_total_fot(
    graph: &Graph<usize, (), Directed>,
    nodes_per_object: usize,
) -> (usize, usize, usize) {
    let mut count = 0;
    let mut reused = 0;
    let mut extptr = 0;
    for node in graph.node_indices() {
        let mut map = HashSet::new();
        let obj_node = node.index() / nodes_per_object;
        for neighbor in graph.neighbors_directed(node, Direction::Outgoing) {
            let obj_neighbor = neighbor.index() / nodes_per_object;

            if obj_neighbor != obj_node {
                extptr += 1;
                if map.insert(obj_neighbor) {
                    count += 1;
                } else {
                    reused += 1;
                }
            }
        }
    }
    (count, reused, extptr)
}

fn weight(a: usize, b: usize, npo: usize) -> f64 {
    let obj_a = (a / npo) + 1;
    let obj_b = (b / npo) + 1;
    let _w = min(a, b) as f64 / max(a, b) as f64;
    let _wo = min(obj_a, obj_b) as f64 / max(obj_a, obj_b) as f64;
    //println!("{} {} {} {}", a, b, w, wo);
    if obj_a == obj_b {
        //return 100.0;
    }
    if a == b {
        return 0.0;
    }
    1.0 / a.abs_diff(b) as f64
}

fn sample<R: Rng + ?Sized>(
    nodes: usize,
    edges: usize,
    npo: usize,
    rng: &mut R,
) -> Graph<usize, (), Directed> {
    let mut graph = Graph::with_capacity(nodes, edges);

    // Add all of our nodes to the graph
    let nodes = Vec::from_iter((0..nodes).map(|i| graph.add_node(i)));

    let all_edges: Vec<_> = nodes
        .iter()
        .cartesian_product(nodes.iter())
        // Don't want to have self-loops, so filter out any (node, node) pairs
        .filter(|(node, other_node)| node != other_node)
        .collect();
    let chosen_edges = all_edges
        .choose_multiple_weighted(rng, edges, |(a, b)| weight(a.index(), b.index(), npo))
        .unwrap();

    for (edge_start, edge_end) in chosen_edges {
        graph.add_edge(**edge_start, **edge_end, ());
    }

    graph
}

fn run(
    nodes: usize,
    edges: usize,
    npo: usize,
) -> (usize, usize, usize, usize, usize, usize, usize, usize, f64) {
    let graph: Graph<usize, (), _> = sample(nodes, edges, npo, &mut thread_rng());
    let tp = calc_total_pointers(&graph);
    let (tf, tr, ext) = calc_total_fot(&graph, npo);
    let int = tp - ext;

    let ra = tf as f64 / tp as f64;

    /*
    println!(
        "{: >12} , {: >12} , {: >12} , {: >12} , {: >12} , {: >12} , {: >12} , {: >12} , {: >12.4}",
        nodes,
        edges,
        graph.node_count() / npo,
        tp,
        tf,
        tr,
        ext,
        int,
        ra
    );
    */
    (
        nodes,
        edges,
        graph.node_count() / npo,
        tp,
        tf,
        tr,
        ext,
        int,
        ra,
    )
}

fn main() {
    use std::thread::available_parallelism;
    let default_parallelism_approx = available_parallelism().unwrap().get();
    eprintln!(
        "Starting thread pool with {} threads",
        default_parallelism_approx
    );
    let pool = ThreadPool::new(default_parallelism_approx);

    let mut total = 0;
    let (tx, rx) = channel();
    for npo in [10, 100] {
        for edges in [1000, 900000] {
            for _trials in 0..1000 {
                let tx = tx.clone();
                total += 1;
                pool.execute(move || {
                    let results = run(1000, edges, npo);
                    tx.send(results).unwrap();
                })
            }
        }
    }
    drop(tx);
    let mut last = 0;
    let mut avg = RealTimeRunningAverage::default();
    while pool.queued_count() + pool.active_count() > 0 {
        let count = pool.queued_count() + pool.active_count();
        let l = last;
        last = count;
        let diff = l.abs_diff(count) as f64;
        let comp = total - count;
        avg.insert(diff as f64);
        eprint!(
            "{: >4.2}% done, {: >12} remaining {: >12}/s                    \r",
            (comp as f64 / total as f64) * 100.0,
            count,
            avg.measurement(),
        );
        std::thread::sleep(Duration::from_millis(100));
    }
    pool.join();
    let mut res: Vec<_> = rx.iter().collect();

    eprintln!("\n\rSorting Results");
    res.sort_by(|a, b| (a.2, a.0, a.1).cmp(&(b.2, b.0, b.1)));
    println!(
        "       NODES ,        EDGES ,      OBJECTS ,   TOTAL_PTRS ,  FOT_ENTRIES ,   REUSED_FOT ,     EXT_PTRS ,     INT_PTRS ,        RATIO"
    );
    for (nodes, edges, objs, tp, tf, tr, ext, int, ra) in res {
        println!(
        "{: >12} , {: >12} , {: >12} , {: >12} , {: >12} , {: >12} , {: >12} , {: >12} , {: >12.4}",
        nodes,
        edges,
        objs,
        tp,
        tf,
        tr,
        ext,
        int,
        ra
    );
    }
}
