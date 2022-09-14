#!/usr/bin/awk -f

BEGIN {
	line = ""
	title = ""
}

line != "" && /%$/ {
	split($0, a, /%/)
	line = sprintf("%s%s", line, a[1])
	next
}

/%$/ {
	split($0, a, /%/)
	line = a[0]
	next
}

/^title=.*[^,]$/ {
	line = $0
	next
}

/\\\\$/ {
	sub(/\\\\/, "\\", $0)
}

line != "" {
	printf("%s%s", line, $0)
	line = ""
	next
}

{
	print
}
