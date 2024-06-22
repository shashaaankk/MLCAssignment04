import graphviz

dot = graphviz.Digraph()

dot.node('mcladhoc-01', shape='square', fontname='arial', fontsize='10', label='mcladhoc-01 \n 192.168.210.60')#60
dot.node('mcladhoc-02', shape='square', fontname='arial', fontsize='10', label='mcladhoc-02 \n 192.168.210.61')#61
dot.node('mcladhoc-03', shape='square', fontname='arial', fontsize='10', label='mcladhoc-03 \n 192.168.210.62')#62
dot.node('mcladhoc-04', shape='square', fontname='arial', fontsize='10', label='mcladhoc-04 \n 192.168.210.63')#63
dot.node('mcladhoc-05', shape='square', fontname='arial', fontsize='10', label='mcladhoc-05 \n 192.168.210.64')#64
dot.node('mcladhoc-06', shape='square', fontname='arial', fontsize='10', label='mcladhoc-06 \n 192.168.210.65')#65
dot.node('mcladhoc-07', shape='square', fontname='arial', fontsize='10', label='mcladhoc-07 \n 192.168.210.66')#66

#WIRELESS LINKS
dot.edge('mcladhoc-01', 'mcladhoc-02', dir='both')

dot.edge('mcladhoc-03', 'mcladhoc-04', dir='both')
dot.edge('mcladhoc-03', 'mcladhoc-05', dir='both')
dot.edge('mcladhoc-03', 'mcladhoc-06', dir='both')
dot.edge('mcladhoc-03', 'mcladhoc-07', dir='both')

dot.edge('mcladhoc-04', 'mcladhoc-05', dir='both')
dot.edge('mcladhoc-04', 'mcladhoc-06', dir='both')
dot.edge('mcladhoc-04', 'mcladhoc-07', dir='both')

dot.edge('mcladhoc-05', 'mcladhoc-06', dir='both')
dot.edge('mcladhoc-05', 'mcladhoc-07', dir='both')

dot.edge('mcladhoc-06', 'mcladhoc-07', dir='both')

dot.render('NetworkTopology', view=True)