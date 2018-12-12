a1 = GetActiveSource()

#plot over line
plotOverLine1 = PlotOverLine(Input=a1,
    Source='High Resolution Line Source')

#select fields
passArrays1 = PassArrays(Input=plotOverLine1)
passArrays1.PointDataArrays = ['U', 'p']

x_list = [0.2, 0.4, 0.6]

for i in range(len(x_list)):
	plotOverLine1.Source.Point1 = [x_list[i], 0.2, 0]
	plotOverLine1.Source.Point2 = [x_list[i], 0.2, 0.4]
	writer = CreateWriter('data_pol_x{0}.csv'.format(x_list[i]))
	writer.UpdatePipeline()
