/* Adjusting bin width
The appearance of a histogram is heavily influenced by the width of its bins: the intervals that determine where each bar lies on the x-axis. If the bins are too wide, you don't see enough detail in the shape of the distribution. If the bins are too narrow, the distribution can be obscured by noise. It's very difficult to know the "best" binwidth, until you physically look at the plot: draw lots of histograms with a range of binwidths until you find one that helps you answer the question.

An agouti eating seeds https://www.notion.so/SQL-0c233d50eb094e9a808e26756686a33d

Here you can see a histogram of agouti (a rodent) sightings from a camera trap on Barra Colorado Island in Panama. When an animal passed the camera, a photo was taken with a timestamp, so the histogram shows the distribution of the time of day when the agouti were most active.

Which of these statements about the agouti activity is true?

Data Source: Rowcliffle et al. 2014: http://dx.doi.org/10.6084/m9.figshare.1160536 */


--Brilliant binwidth adjustment! Choosing an appropriate binwidth make it easier to interpret the histogram.