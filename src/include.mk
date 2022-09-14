
gendata/fotoverhead-out: src/fot_overhead/* src/fot_overhead/src/*
	@mkdir -p gendata
	cd src/fot_overhead && cargo run --release > ../../gendata/fotoverhead-out