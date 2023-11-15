# Look through the text and mark the statements as true (T) or false (F). If you think a statement is false, change it to make it true.

1.	Computers that store and manage information electronically have replaced file cabinets and mountains of papers.(T)
2.	The public Internet forbids businesses around the world to share information with each other and their customers.(F) It allows them to do that.
3.	The Internet is the most conspicuous example of computer networking.(T)
4.	The card catalogues weren't replaced with computer terminals in the public libraries.(F) They were.
5.	LAN technologies connect a smaller number of devices that can be many kilometers apart.(F) No, the devices should be near each other for the network to be called a LAN.
6.	WAN technologies connect many devices that are relatively close to each other.(F) The devices should be farther apart.
7.	In comparison to WANs, LANs are faster and more reliable.(T)
8.	Fiber optic cables have given LAN technologies an opportunity to connect devices thousands of kilometers apart.(F) WAN
9.	In 1973 at IBM Corporation, researcher Bob Metcalfe designed and tested the first Ethernet network.(F) Xerox Corporation
10.	Ethernet has since become the least popular and least deployed network technology in the world.(F) The opposite
11.	Once a device attached to the Ethernet, it had the ability to communicate with any other attached device.(T)
12.	At most, Ethernet devices could have only a few hundred meters of cable between them.(T)
13.	Historically, the medium has been a twisted pair or fiber optic cable, but today it is more commonly a coaxial copper cabling.(F) The opposite.
14.	Frames are analogous to sentences in human language.(T)
15.	There are no explicit minimum and maximum lengths for frames.(F) The opposite.
16.	Each frame must include only a destination address, which identifies the recipient of the message.(F) The sender address is also needed along with some other data like a check sum.
17.	The destination address is of no importance in identifying the intended recipient of the frame. (F) The opposite.
18.	The station discards the frame without even examining its contents if the frame is not intended for this station.(T)
19.	A frame with a destination address equal to the broadcast address is not intended for every node, but for specific station on the network.(F) The opposite, it's literally in the name.
20.	The CSMA/CD describes how the Ethernet protocol regulates communication among nodes.(T)
21.	If the medium is quiet, the station knows that it should wait before transmitting.(F) The station waits if somebody else is transmiting (the medium is not quiet).
22.	If a station hears its own transmission returning in a garbled form, then it knows that everything was OK.(F) The opposite.
23.	A single Ethernet segment is sometimes called a collision domain because no two stations on the segment can transmit at the same time without causing a collision.(T)
24.	If two stations collide when transmitting once, then both will not transmit the same data again.(F) They will try to transmit their data after a short but random delay (or several of those if collisions keep happening).
25.	A primary practical limitation concerns the length of the shared cable.(T)
26.	Electrical interference from neighboring devices can intensify the signal.(F) Nope, it interferes with the signal. (I guess if the stars a right then it can intensify it but the probability is incredibly small.)
27.	Network diameter is a practical limit to the number of devices that can coexist in a single network.(F) If you don't have repeaters, which are included into all of the modern networking equipment, then yes.
28.	Using repeaters, you can significantly increase your network diameter.(T) Ah, I refered to repeaters prematurely in the question above.
29.	When a number of stations connected to the same segment increased, Ethernet networks faced congestion problems.(T)
30.	To alleviate problems with transmission speed Ethernet network implemented bridges.(F) Bridges solve the segmentation problem. You need better cable for better speed.
31.	One goal of the bridge is to reduce any traffic on both segments.(T) Yep, with bridges the traffic that isn't directed at the other segmens doesn't reach them.
32.	While Ethernet broadcasts cross bridges, they do not cross routers, because the router forms a logical boundary for the network.(T)
