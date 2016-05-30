from PlanElementGraph import *

excavate = Operator(id = 1, type = 'Action', name = 'excavate', num_args = 3)
p1 = Literal(id=2, type='Condition', name= 'alive', num_args = 1, truth = True)
p2 = Literal(id=3, type='Condition', name= 'at', num_args = 2, truth = True)
p3 = Literal(id=4, type='Condition', name= 'burried', num_args = 2, truth = True)
p4 = Literal(id=5, type='Condition', name= 'knows-location', num_args = 3, truth = True)

e1 = Literal(id=6, type='Condition', name='burried', num_args=2, truth = False)
e2 = Literal(id=7, type='Condition', name='has', num_args=2, truth = True)

consent = Argument(id=8, type='actor', name=None, arg_pos_dict = {excavate.id: 1})
item = Argument(id = 9, type='var', name=None, arg_pos_dict={excavate.id : 2})
place = Argument(id = 10, type='var', name=None,arg_pos_dict= {excavate.id : 3})

edge0 = Edge(excavate, consent, 'actor-of')
edge1 = Edge(excavate, p1, 'precond-of')
edge2 = Edge(excavate, p2, 'precond-of')
edge3 = Edge(excavate, p3, 'precond-of')
edge4 = Edge(excavate, p4, 'precond-of')

edge5 = Edge(excavate, e1, 'effect-of')
edge6 = Edge(excavate, e2, 'effect-of')

edge7 = Edge(p1, consent, 'first-arg')
edge8 = Edge(p2, consent, 'first-arg')
edge9 = Edge(p4, consent, 'first-arg')
edge10 = Edge(e2, consent, 'first-arg')

edge12 = Edge(p2, item, 'sec-arg')
edge13 = Edge(p3, item, 'first-arg')
edge14 = Edge(p4, item, 'sec-arg')
edge15 = Edge(e1, item, 'first-arg')
edge16 = Edge(e2, item, 'sec-arg')

edge17 = Edge(p2, place, 'sec-arg')
edge18 = Edge(p3, place, 'sec-arg')
edge19 = Edge(p4, place, 'third-arg')
edge20 = Edge(e1, place, 'sec-arg')

excavate_elements = {excavate, p1, p2, p3, p4, e1, e2, consent, item, place}
excavate_edges = {edge0, edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, \
					edge12, edge13, edge14,edge15, edge16,edge17, edge18, edge19, edge20}

####Operator - Domain Action
Excavate_graph = ElementGraph(	id = 0,\
								type = 'Action', \
								name = 'excavate', \
								Elements = excavate_elements, \
								root_element = excavate,\
								Edges = excavate_edges)

example = Operator(id = 111, type= 'Action')
example_p1 = Literal(id=211, type='Condition', name='alive', truth = True)
example_e1 = Literal(id=311, type = 'Condition', name='has', truth = True)
example_actor = Argument(id=411, type='actor',arg_pos_dict={example.id : 1})
example_item = Argument(id=511,type='var', arg_pos_dict={})
#arg_pos_dict={example.id : 0})

example_edge0 = Edge(example, example_p1, 'precond-of')
example_edge1 = Edge(example, example_e1, 'effect-of')
example_edge2 = Edge(example_p1, example_actor, 'first-arg')
example_edge3 = Edge(example_e1, example_actor, 'first-arg')
example_edge4 = Edge(example_e1, example_item, 'sec-arg')

#Cannot have a precondition with name 'knows-location', first-arg is actor, sec-arg is item
#Since we know this is precondition of excavate, the example_graph should not be consistent
example_constraint_Literal = Literal(id=6, type ='Condition', name='knows-location', truth = True)
example_constraint_edge0 = Edge(example_constraint_Literal, example_actor, 'first-arg')
example_constraint_edge1 = Edge(example_constraint_Literal, example_item, 'sec-arg')

example_elements = {example, example_p1, example_e1, example_actor, example_item,example_constraint_Literal}
example_edges = {example_edge0, example_edge1, example_edge2, example_edge3, example_edge4}
example_constraints = {example_constraint_edge0, example_constraint_edge1}

#### Partial-step Action/DomainOperator?
Example_graph = ElementGraph(	id = 1111, \
								type='Action', \
								Elements = example_elements, \
								root_element = example,\
								Edges = example_edges, \
								Constraints = example_constraints)

print('consistent: ', Excavate_graph.isConsistent(Example_graph))