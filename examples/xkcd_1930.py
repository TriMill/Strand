import sys
sys.path.insert(0, '../src')
import strand

# Text generator for xkcd comic 1930 "Calendar Facts"
# https://xkcd.com/1930/

print(strand.parse('Did you know that [\
the [fall|spring] equinox|\
the [winter|summer] [solstice|Olympics]|\
the [earliest|latest] [sunrise|sunset]|\
daylight [saving|savings] time|\
leap [day|year]|\
easter|\
the [harvest|super|blood] moon|\
Toyota Truck Month|\
Shark Week] \
[happens [earlier|later|at the wrong time] every year|\
drifts out of sync with the [sun|moon|zodiac|[Gregorian|Mayan|lunar|iPhone]\
calendar|atomic clock in Colorado]|\
might [not happen|happen twice] this year] \
because of [time zone legislation in [Indiana|Arizona|Russia]|\
a decree by the Pope in the 1500s|\
[precession|libration|nutation|libation|eccentricity|obliquity] of the \
[moon|sun|earth\'s axis|equator|prime meridian|International Date Line|Mason-Dixon line]|\
magnetic field reversal|\
an arbitrary desicion by [Benjamin Franklin|Isaac Newton|FDR]]? \
Apparently [it causes a predictable increase in car accidents|\
that\'s why we have leap seconds|\
scientists are really worried|\
it was even more extreme during the [Bronze Age|Ice Age|Cretaceous|1990s]|\
there\'s a proposal to fix it, but it \
[will never happen|actually makes things worse|is stalled in Congress|might be unconstitutional]|\
it\'s getting worse and nobody knows why].'))
