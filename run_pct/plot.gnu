# Plot percentage of time spent running
# PSK, October 2024

set xdata time
set timefmt '%Y-%m-%d'
set datafile sep ','
set yrange [0:100]
set ytics 10
set grid
set key

plot 'run.txt' using 1:2 with linespoints title "Run pct"

