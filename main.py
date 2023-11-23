import plotly.graph_objects as go
label = ['Revenue(0)','Cost of revenue(1)','Gross Margin(2)','SG&A Expenses(3)',
         'Operating income(4)','Other income(5)','Income before income taxes(6)','Income taxes(7)',
         'Income after income taxes(8)','Non-controlling interests(9)','Net Income(10)']
value  = [302870,203040,76760,126280,126280,7360,34050,99590,330,99260]
#node_labels = [f"{label[i]}: {value[i]}" for i in range(len(label))]
source = [0,0,2,2,4,5,6,6,8,8]
target = [1,2,3,4,6,6,7,8,9,10]
link=dict(source=source,target=target,value=value)
node=dict(label=label,pad=100,thickness=25)
data=go.Sankey(link=link,node=node)
print(data)
#plot sankey chart----------
fig=go.Figure(data)
fig.update_layout(title = 'Tata Consultancy Services - Income Statement',
                  font=dict(size=14,color='green'),
                  )
fig.show()