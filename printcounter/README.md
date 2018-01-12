printcounter1: The starting point. Non concurrent code.
printcounter2: Non concurrent code refactored to use functions
printcounter3: First concurrent attempt. Run multiple threads. It looks like it works but it actually doesn't
printcounter4: Addes fuzz to previous example to demostrate how it fails.
printcounter5: Concurrent code using atomic queues to solve the problem
printcounter6: Concurrent code using atomic queues without fuzz logic
printcounter7: Concurrent code using locks.
printcounter8: Concurrent code using locks without fuzz logic


Notice printcounter8 is simpler than printcounter5, however the locks don't actually lock the print command.
In the example using queues, a print manager is introduced to have exclusive access to the print command (controlling the shared resource to ensure sequence).