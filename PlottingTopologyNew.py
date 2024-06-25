import graphviz

dot = graphviz.Digraph()

dot.node('mcladhoc-01', shape='square', fontname='arial', fontsize='10', label='mcladhoc-01 \n 192.168.210.60')#60
dot.node('mcladhoc-02', shape='square', fontname='arial', fontsize='10', label='mcladhoc-02 \n 192.168.210.61')#61
dot.node('mcladhoc-03', shape='square', fontname='arial', fontsize='10', label='mcladhoc-03 \n 192.168.210.62', color='gray')#62
dot.node('mcladhoc-04', shape='square', fontname='arial', fontsize='10', label='mcladhoc-04 \n 192.168.210.63')#63
dot.node('mcladhoc-05', shape='square', fontname='arial', fontsize='10', label='mcladhoc-05 \n 192.168.210.64')#64
dot.node('mcladhoc-06', shape='square', fontname='arial', fontsize='10', label='mcladhoc-06 \n 192.168.210.65')#65
dot.node('mcladhoc-07', shape='square', fontname='arial', fontsize='10', label='mcladhoc-07 \n 192.168.210.66')#66

#WIRELESS LINKS

dot.edge('mcladhoc-07', 'mcladhoc-06', label='~7.7ms*', dir='both', fontsize='8') #66-65, 65-66
dot.edge('mcladhoc-07', 'mcladhoc-05', label='~8.5ms*', dir='both', fontsize='8') #66-64, 64-66
dot.edge('mcladhoc-05', 'mcladhoc-04', label='~9.5ms*', fontsize='8', dir='both')  #64-63, 63-64
dot.edge('mcladhoc-06', 'mcladhoc-05', label='~9.4ms*', dir='both', fontsize='8') #65-64, 64-65

dot.edge('mcladhoc-05', 'mcladhoc-03', label='~13.3ms*', fontsize='8') #64-62
dot.edge('mcladhoc-01', 'mcladhoc-03', label='~16.5ms*', fontsize='8') #60-62
dot.edge('mcladhoc-04', 'mcladhoc-03', label='~8.0ms*', fontsize='8')  #63-62

dot.edge('mcladhoc-01', 'mcladhoc-02', dir='both', label='~170ms*', fontsize='8')#60-61,61-60

# dot.edge('mcladhoc-06', 'mcladhoc-07', label='~7.78ms') #65-66
# dot.edge('mcladhoc-06', 'mcladhoc-05', label='~8.85ms') #65-64

# dot.edge('mcladhoc-05', 'mcladhoc-07', label='~7.78ms') #64-66
# dot.edge('mcladhoc-05', 'mcladhoc-06', label='~8.85ms') #64-65
# dot.edge('mcladhoc-05', 'mcladhoc-04', label='~7.78ms') #64-63
# dot.edge('mcladhoc-05', 'mcladhoc-03', label='~8.85ms') #64-62

# dot.edge('mcladhoc-01', 'mcladhoc-03', dir='both', label='7.78ms')
# dot.edge('mcladhoc-03', 'mcladhoc-04', dir='both')
# dot.edge('mcladhoc-03', 'mcladhoc-05', dir='both')
# #dot.edge('mcladhoc-03', 'mcladhoc-06', dir='both')
# #dot.edge('mcladhoc-03', 'mcladhoc-07', dir='both')

# dot.edge('mcladhoc-04', 'mcladhoc-05', dir='both')
# dot.edge('mcladhoc-04', 'mcladhoc-06', dir='both')
# dot.edge('mcladhoc-04', 'mcladhoc-07', dir='both')

# dot.edge('mcladhoc-05', 'mcladhoc-06', dir='both')
# dot.edge('mcladhoc-05', 'mcladhoc-07', dir='both')

# dot.edge('mcladhoc-06', 'mcladhoc-07', dir='both')

dot.render('NetworkTopology', view=True)