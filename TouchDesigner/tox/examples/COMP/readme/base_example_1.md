TouchDesigner is a "pull system". A common misconception with cooking in TouchDesigner is that cooking starts upstream and moves downstream. This is incorrect. Almost all operators will only cook when something is interested in their data. 

This example shows this behavior, and how you can use it to heavily optimize your networks.

* Notice the Info CHOPs showing when children nodes in a Base COMP are cooking. When output from a base is not requested, all cooking of all children in that Base COMP stops (except when data is forced out like with an Audio Device Out CHOP).

* Looking at the wires from the Base COMPs to the Switch TOP, notice how only the wire from the Base COMP which output is requested is animated, which means that content is cooking. The other 2 wires are static which indicates nothing is cooking inside them. 

Now activate the viewer pane of Base3 (top left circle icon on Base3 node). Notice how Base3 now keeps cooking - this is because you are requesting output by viewing its contents.
