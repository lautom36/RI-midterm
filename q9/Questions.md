#9. (20 points) Ethics of Robotics - Open Ended Questions

(a) (5 points) Many people (particularly those in the robotics industry) believe that robotics is purely within the purview of technical development and should not have any ethical considerations. What do you feel can be a merit or demerit to this way of thinking?

As with anything, there are always bad actors intent on abusing technology that can be a detriment to personal or societal safety. Those considerations are important but ultimately won't impede the progress of technological development. If anything, responsible invention should be encouraged so that the good uses of the technology are put forward with safeguards against misuse. Robotics is no exception.


(b) (5 points) Isaac Asimov listed 3 laws of robotics, comment on the algorithmic complexity of implementing these into working intelligence. Define a scenario and write Psuedo code to implement these rules.

The Laws are written in a hierarchical way so that no harm is done to a human being. Since preventing harm is the first priority, it has to be calculated first and any other function of the robot is secondary to that. Identifying harm is a difficult proposition on its own. For this scenario we consider direct physical personal harm only, meaning only harm that the robot can perpetrate and prevent as far as it is aware. We'll use a spot welding arm working in a car manufacturing plant as our subject. Suppose a worker falls into a car frame on its way to be welded.

````
// Checks that the workspace is only metallic or other nonorganic material.
// This is the quickest way to determine if a harmable object composed of nonmetallic material could be where it shouldn't be.
// Probably relies on a RADAR sensor of some sort.
VerifyMaterial() {
    [Scanning activities]
    ...
    if (scan.material != expected.material) EmergencyStop();
    else { [Continue] }
 }

// If the worker was wearing some metallic garb that could trick the previous check for some reason, this will check for an expected layout or orientation of the car frame.
// The person should trigger EmergencyStop() so long as the scanners are pervasive enough to sufficiently check every cavity that a human could occupy.
// This is also good for checking that the frame is in the correct position to be welded.
VerifyOrientation() {
    [Scanning activities]
    ...
    if (scan.orientation != expected.layout) EmergencyStop();
    else { [Continue] }
}

EmergencyStop() {
    // First, power to the tip needs to be cut to prevent burns in case it ends up making contact with the person at some point during the stopping procedure.
    TerminateWeld();

    // Second, if the robot is hooked up to an integrated watchdog for the whole assembly line, send a signal to it.
    parent.FullStop();

    // Lastly, the robot needs to pull itself out of the way if the line isn't able to stop, probably its rest position.
    // The limp parameter is so that it responds to any outside pressure by giving way. If it is still in the way, the object will be able to push past it without much resistance.
    GoToDefaultPose(limp=true);
}
````


(c) (5 points) In the event of an autonomous system causing harm or damages, who is responsible? Read and comment on the following two documents: https://www.callahan-law.com/articles-and-expert-advice/when-an-autonomous-vehicle-hits-a-pedestrian-who-is-responsible/ and https://en.wikipedia.org/wiki/Self-driving_car_liability

(d) (5 points) What laws may be helpful for regulating or controlling autonomous systems? What drawbacks will this potentially have?

The Callahan Law article seems to put the liability on a backup driver, if there is one, then on the manufacturers. The Wikipedia entry added some product liability perspectives. Normally, a user of a product accepts all the risk of operating a product and any hidden or excessive risk is made known by the manufacturer. When the user of an autonomous vehicle isn't directly operating, the question seems to fall on how can the manufacturer minimize their liability. Likely it is to completely disclose and minimize risk of using the product, which is backed by precedence. Of course, strict liability on performance of autonomous vehicles narrows the competitive market or extensively lengthens R&D time so that is not reasonably an option if states wish for advances in the field. Perhaps one of the closest precedences for autonomous vehicles is minor law. A parent or guardian has responsibility for a child even though the child acts as an independent actor. Although more of minor law deals with negligence of care, the same principles could be applied to owners of autonomous vehicles. Ensuring the car is in good repair is a charge of the owner/operator so any accident caused, wholly or in part, by an issue resolvable by the owner/operator is the owner/operator's fault. There are also defects that happen in the manufacturing plant that may be at fault and the liability would lie on the quality control of the manufacturer. The same applies to the developers of the technology if it failed to sense a common or expected edge case.
