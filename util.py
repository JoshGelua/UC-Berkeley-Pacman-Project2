# util.py
# -------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).
from __future__ import print_function

import heapq
import inspect
import random
import signal
import sys
import time

if sys.version_info > (3,):
    long = int


class FixedRandom:
    def __init__(self):
        fixedState = (
            3,
            (
                long(2147483648),
                long(507801126),
                long(683453281),
                long(310439348),
                long(2597246090),
                long(2209084787),
                long(2267831527),
                long(979920060),
                long(3098657677),
                long(37650879),
                long(807947081),
                long(3974896263),
                long(881243242),
                long(3100634921),
                long(1334775171),
                long(3965168385),
                long(746264660),
                long(4074750168),
                long(500078808),
                long(776561771),
                long(702988163),
                long(1636311725),
                long(2559226045),
                long(157578202),
                long(2498342920),
                long(2794591496),
                long(4130598723),
                long(496985844),
                long(2944563015),
                long(3731321600),
                long(3514814613),
                long(3362575829),
                long(3038768745),
                long(2206497038),
                long(1108748846),
                long(1317460727),
                long(3134077628),
                long(988312410),
                long(1674063516),
                long(746456451),
                long(3958482413),
                long(1857117812),
                long(708750586),
                long(1583423339),
                long(3466495450),
                long(1536929345),
                long(1137240525),
                long(3875025632),
                long(2466137587),
                long(1235845595),
                long(4214575620),
                long(3792516855),
                long(657994358),
                long(1241843248),
                long(1695651859),
                long(3678946666),
                long(1929922113),
                long(2351044952),
                long(2317810202),
                long(2039319015),
                long(460787996),
                long(3654096216),
                long(4068721415),
                long(1814163703),
                long(2904112444),
                long(1386111013),
                long(574629867),
                long(2654529343),
                long(3833135042),
                long(2725328455),
                long(552431551),
                long(4006991378),
                long(1331562057),
                long(3710134542),
                long(303171486),
                long(1203231078),
                long(2670768975),
                long(54570816),
                long(2679609001),
                long(578983064),
                long(1271454725),
                long(3230871056),
                long(2496832891),
                long(2944938195),
                long(1608828728),
                long(367886575),
                long(2544708204),
                long(103775539),
                long(1912402393),
                long(1098482180),
                long(2738577070),
                long(3091646463),
                long(1505274463),
                long(2079416566),
                long(659100352),
                long(839995305),
                long(1696257633),
                long(274389836),
                long(3973303017),
                long(671127655),
                long(1061109122),
                long(517486945),
                long(1379749962),
                long(3421383928),
                long(3116950429),
                long(2165882425),
                long(2346928266),
                long(2892678711),
                long(2936066049),
                long(1316407868),
                long(2873411858),
                long(4279682888),
                long(2744351923),
                long(3290373816),
                long(1014377279),
                long(955200944),
                long(4220990860),
                long(2386098930),
                long(1772997650),
                long(3757346974),
                long(1621616438),
                long(2877097197),
                long(442116595),
                long(2010480266),
                long(2867861469),
                long(2955352695),
                long(605335967),
                long(2222936009),
                long(2067554933),
                long(4129906358),
                long(1519608541),
                long(1195006590),
                long(1942991038),
                long(2736562236),
                long(279162408),
                long(1415982909),
                long(4099901426),
                long(1732201505),
                long(2934657937),
                long(860563237),
                long(2479235483),
                long(3081651097),
                long(2244720867),
                long(3112631622),
                long(1636991639),
                long(3860393305),
                long(2312061927),
                long(48780114),
                long(1149090394),
                long(2643246550),
                long(1764050647),
                long(3836789087),
                long(3474859076),
                long(4237194338),
                long(1735191073),
                long(2150369208),
                long(92164394),
                long(756974036),
                long(2314453957),
                long(323969533),
                long(4267621035),
                long(283649842),
                long(810004843),
                long(727855536),
                long(1757827251),
                long(3334960421),
                long(3261035106),
                long(38417393),
                long(2660980472),
                long(1256633965),
                long(2184045390),
                long(811213141),
                long(2857482069),
                long(2237770878),
                long(3891003138),
                long(2787806886),
                long(2435192790),
                long(2249324662),
                long(3507764896),
                long(995388363),
                long(856944153),
                long(619213904),
                long(3233967826),
                long(3703465555),
                long(3286531781),
                long(3863193356),
                long(2992340714),
                long(413696855),
                long(3865185632),
                long(1704163171),
                long(3043634452),
                long(2225424707),
                long(2199018022),
                long(3506117517),
                long(3311559776),
                long(3374443561),
                long(1207829628),
                long(668793165),
                long(1822020716),
                long(2082656160),
                long(1160606415),
                long(3034757648),
                long(741703672),
                long(3094328738),
                long(459332691),
                long(2702383376),
                long(1610239915),
                long(4162939394),
                long(557861574),
                long(3805706338),
                long(3832520705),
                long(1248934879),
                long(3250424034),
                long(892335058),
                long(74323433),
                long(3209751608),
                long(3213220797),
                long(3444035873),
                long(3743886725),
                long(1783837251),
                long(610968664),
                long(580745246),
                long(4041979504),
                long(201684874),
                long(2673219253),
                long(1377283008),
                long(3497299167),
                long(2344209394),
                long(2304982920),
                long(3081403782),
                long(2599256854),
                long(3184475235),
                long(3373055826),
                long(695186388),
                long(2423332338),
                long(222864327),
                long(1258227992),
                long(3627871647),
                long(3487724980),
                long(4027953808),
                long(3053320360),
                long(533627073),
                long(3026232514),
                long(2340271949),
                long(867277230),
                long(868513116),
                long(2158535651),
                long(2487822909),
                long(3428235761),
                long(3067196046),
                long(3435119657),
                long(1908441839),
                long(788668797),
                long(3367703138),
                long(3317763187),
                long(908264443),
                long(2252100381),
                long(764223334),
                long(4127108988),
                long(384641349),
                long(3377374722),
                long(1263833251),
                long(1958694944),
                long(3847832657),
                long(1253909612),
                long(1096494446),
                long(555725445),
                long(2277045895),
                long(3340096504),
                long(1383318686),
                long(4234428127),
                long(1072582179),
                long(94169494),
                long(1064509968),
                long(2681151917),
                long(2681864920),
                long(734708852),
                long(1338914021),
                long(1270409500),
                long(1789469116),
                long(4191988204),
                long(1716329784),
                long(2213764829),
                long(3712538840),
                long(919910444),
                long(1318414447),
                long(3383806712),
                long(3054941722),
                long(3378649942),
                long(1205735655),
                long(1268136494),
                long(2214009444),
                long(2532395133),
                long(3232230447),
                long(230294038),
                long(342599089),
                long(772808141),
                long(4096882234),
                long(3146662953),
                long(2784264306),
                long(1860954704),
                long(2675279609),
                long(2984212876),
                long(2466966981),
                long(2627986059),
                long(2985545332),
                long(2578042598),
                long(1458940786),
                long(2944243755),
                long(3959506256),
                long(1509151382),
                long(325761900),
                long(942251521),
                long(4184289782),
                long(2756231555),
                long(3297811774),
                long(1169708099),
                long(3280524138),
                long(3805245319),
                long(3227360276),
                long(3199632491),
                long(2235795585),
                long(2865407118),
                long(36763651),
                long(2441503575),
                long(3314890374),
                long(1755526087),
                long(17915536),
                long(1196948233),
                long(949343045),
                long(3815841867),
                long(489007833),
                long(2654997597),
                long(2834744136),
                long(417688687),
                long(2843220846),
                long(85621843),
                long(747339336),
                long(2043645709),
                long(3520444394),
                long(1825470818),
                long(647778910),
                long(275904777),
                long(1249389189),
                long(3640887431),
                long(4200779599),
                long(323384601),
                long(3446088641),
                long(4049835786),
                long(1718989062),
                long(3563787136),
                long(44099190),
                long(3281263107),
                long(22910812),
                long(1826109246),
                long(745118154),
                long(3392171319),
                long(1571490704),
                long(354891067),
                long(815955642),
                long(1453450421),
                long(940015623),
                long(796817754),
                long(1260148619),
                long(3898237757),
                long(176670141),
                long(1870249326),
                long(3317738680),
                long(448918002),
                long(4059166594),
                long(2003827551),
                long(987091377),
                long(224855998),
                long(3520570137),
                long(789522610),
                long(2604445123),
                long(454472869),
                long(475688926),
                long(2990723466),
                long(523362238),
                long(3897608102),
                long(806637149),
                long(2642229586),
                long(2928614432),
                long(1564415411),
                long(1691381054),
                long(3816907227),
                long(4082581003),
                long(1895544448),
                long(3728217394),
                long(3214813157),
                long(4054301607),
                long(1882632454),
                long(2873728645),
                long(3694943071),
                long(1297991732),
                long(2101682438),
                long(3952579552),
                long(678650400),
                long(1391722293),
                long(478833748),
                long(2976468591),
                long(158586606),
                long(2576499787),
                long(662690848),
                long(3799889765),
                long(3328894692),
                long(2474578497),
                long(2383901391),
                long(1718193504),
                long(3003184595),
                long(3630561213),
                long(1929441113),
                long(3848238627),
                long(1594310094),
                long(3040359840),
                long(3051803867),
                long(2462788790),
                long(954409915),
                long(802581771),
                long(681703307),
                long(545982392),
                long(2738993819),
                long(8025358),
                long(2827719383),
                long(770471093),
                long(3484895980),
                long(3111306320),
                long(3900000891),
                long(2116916652),
                long(397746721),
                long(2087689510),
                long(721433935),
                long(1396088885),
                long(2751612384),
                long(1998988613),
                long(2135074843),
                long(2521131298),
                long(707009172),
                long(2398321482),
                long(688041159),
                long(2264560137),
                long(482388305),
                long(207864885),
                long(3735036991),
                long(3490348331),
                long(1963642811),
                long(3260224305),
                long(3493564223),
                long(1939428454),
                long(1128799656),
                long(1366012432),
                long(2858822447),
                long(1428147157),
                long(2261125391),
                long(1611208390),
                long(1134826333),
                long(2374102525),
                long(3833625209),
                long(2266397263),
                long(3189115077),
                long(770080230),
                long(2674657172),
                long(4280146640),
                long(3604531615),
                long(4235071805),
                long(3436987249),
                long(509704467),
                long(2582695198),
                long(4256268040),
                long(3391197562),
                long(1460642842),
                long(1617931012),
                long(457825497),
                long(1031452907),
                long(1330422862),
                long(4125947620),
                long(2280712485),
                long(431892090),
                long(2387410588),
                long(2061126784),
                long(896457479),
                long(3480499461),
                long(2488196663),
                long(4021103792),
                long(1877063114),
                long(2744470201),
                long(1046140599),
                long(2129952955),
                long(3583049218),
                long(4217723693),
                long(2720341743),
                long(820661843),
                long(1079873609),
                long(3360954200),
                long(3652304997),
                long(3335838575),
                long(2178810636),
                long(1908053374),
                long(4026721976),
                long(1793145418),
                long(476541615),
                long(973420250),
                long(515553040),
                long(919292001),
                long(2601786155),
                long(1685119450),
                long(3030170809),
                long(1590676150),
                long(1665099167),
                long(651151584),
                long(2077190587),
                long(957892642),
                long(646336572),
                long(2743719258),
                long(866169074),
                long(851118829),
                long(4225766285),
                long(963748226),
                long(799549420),
                long(1955032629),
                long(799460000),
                long(2425744063),
                long(2441291571),
                long(1928963772),
                long(528930629),
                long(2591962884),
                long(3495142819),
                long(1896021824),
                long(901320159),
                long(3181820243),
                long(843061941),
                long(3338628510),
                long(3782438992),
                long(9515330),
                long(1705797226),
                long(953535929),
                long(764833876),
                long(3202464965),
                long(2970244591),
                long(519154982),
                long(3390617541),
                long(566616744),
                long(3438031503),
                long(1853838297),
                long(170608755),
                long(1393728434),
                long(676900116),
                long(3184965776),
                long(1843100290),
                long(78995357),
                long(2227939888),
                long(3460264600),
                long(1745705055),
                long(1474086965),
                long(572796246),
                long(4081303004),
                long(882828851),
                long(1295445825),
                long(137639900),
                long(3304579600),
                long(2722437017),
                long(4093422709),
                long(273203373),
                long(2666507854),
                long(3998836510),
                long(493829981),
                long(1623949669),
                long(3482036755),
                long(3390023939),
                long(833233937),
                long(1639668730),
                long(1499455075),
                long(249728260),
                long(1210694006),
                long(3836497489),
                long(1551488720),
                long(3253074267),
                long(3388238003),
                long(2372035079),
                long(3945715164),
                long(2029501215),
                long(3362012634),
                long(2007375355),
                long(4074709820),
                long(631485888),
                long(3135015769),
                long(4273087084),
                long(3648076204),
                long(2739943601),
                long(1374020358),
                long(1760722448),
                long(3773939706),
                long(1313027823),
                long(1895251226),
                long(4224465911),
                long(421382535),
                long(1141067370),
                long(3660034846),
                long(3393185650),
                long(1850995280),
                long(1451917312),
                long(3841455409),
                long(3926840308),
                long(1397397252),
                long(2572864479),
                long(2500171350),
                long(3119920613),
                long(531400869),
                long(1626487579),
                long(1099320497),
                long(407414753),
                long(2438623324),
                long(99073255),
                long(3175491512),
                long(656431560),
                long(1153671785),
                long(236307875),
                long(2824738046),
                long(2320621382),
                long(892174056),
                long(230984053),
                long(719791226),
                long(2718891946),
                long(624),
            ),
            None,
        )
        self.random = random.Random()
        self.random.setstate(fixedState)


"""
 Data structures useful for implementing SearchAgents
"""


class Stack:
    "A container with a last-in-first-out (LIFO) queuing policy."

    def __init__(self):
        self.list = []

    def push(self, item):
        "Push 'item' onto the stack"
        self.list.append(item)

    def pop(self):
        "Pop the most recently pushed item from the stack"
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the stack is empty"
        return len(self.list) == 0


class Queue:
    "A container with a first-in-first-out (FIFO) queuing policy."

    def __init__(self):
        self.list = []

    def push(self, item):
        "Enqueue the 'item' into the queue"
        self.list.insert(0, item)

    def pop(self):
        """
          Dequeue the earliest enqueued item still in the queue. This
          operation removes the item from the queue.
        """
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the queue is empty"
        return len(self.list) == 0


class PriorityQueue:
    """
      Implements a priority queue data structure. Each inserted item
      has a priority associated with it and the client is usually interested
      in quick retrieval of the lowest-priority item in the queue. This
      data structure allows O(1) access to the lowest-priority item.

      Note that this PriorityQueue does not allow you to change the priority
      of an item.  However, you may insert the same item multiple times with
      different priorities.
    """

    def __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        # FIXME: restored old behaviour to check against old results better
        # FIXED: restored to stable behaviour
        entry = (priority, self.count, item)
        # entry = (priority, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        #  (_, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0


class PriorityQueueWithFunction(PriorityQueue):
    """
    Implements a priority queue with the same push/pop signature of the
    Queue and the Stack classes. This is designed for drop-in replacement for
    those two classes. The caller has to provide a priority function, which
    extracts each item's priority.
    """

    def __init__(self, priorityFunction):
        "priorityFunction (item) -> priority"
        self.priorityFunction = priorityFunction  # store the priority function
        PriorityQueue.__init__(self)  # super-class initializer

    def push(self, item):
        "Adds an item to the queue with priority from the priority function"
        PriorityQueue.push(self, item, self.priorityFunction(item))


def manhattanDistance(xy1, xy2):
    "Returns the Manhattan distance between points xy1 and xy2"
    return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])


"""
  Data structures and functions useful for various course projects

  The search project should not need anything below this line.
"""


class Counter(dict):
    """
    A counter keeps track of counts for a set of keys.

    The counter class is an extension of the standard python
    dictionary type.  It is specialized to have number values
    (integers or floats), and includes a handful of additional
    functions to ease the task of counting data.  In particular,
    all keys are defaulted to have value 0.  Using a dictionary:

    a = {}
    print a['test']

    would give an error, while the Counter class analogue:

    >>> a = Counter()
    >>> print a['test']
    0

    returns the default 0 value. Note that to reference a key
    that you know is contained in the counter,
    you can still use the dictionary syntax:

    >>> a = Counter()
    >>> a['test'] = 2
    >>> print a['test']
    2

    This is very useful for counting things without initializing their counts,
    see for example:

    >>> a['blah'] += 1
    >>> print a['blah']
    1

    The counter also includes additional functionality useful in implementing
    the classifiers for this assignment.  Two counters can be added,
    subtracted or multiplied together.  See below for details.  They can
    also be normalized and their total count and arg max can be extracted.
    """

    def __getitem__(self, idx):
        self.setdefault(idx, 0)
        return dict.__getitem__(self, idx)

    def incrementAll(self, keys, count):
        """
        Increments all elements of keys by the same count.

        >>> a = Counter()
        >>> a.incrementAll(['one','two', 'three'], 1)
        >>> a['one']
        1
        >>> a['two']
        1
        """
        for key in keys:
            self[key] += count

    def argMax(self):
        """
        Returns the key with the highest value.
        """
        if len(self) == 0:
            return None
        all = list(self.items())
        values = [x[1] for x in all]
        maxIndex = values.index(max(values))
        return all[maxIndex][0]

    def sortedKeys(self):
        """
        Returns a list of keys sorted by their values.  Keys
        with the highest values will appear first.

        >>> a = Counter()
        >>> a['first'] = -2
        >>> a['second'] = 4
        >>> a['third'] = 1
        >>> a.sortedKeys()
        ['second', 'third', 'first']
        """
        sortedItems = list(self.items())

        def compare(x, y):
            return sign(y[1] - x[1])

        sortedItems.sort(cmp=compare)
        return [x[0] for x in sortedItems]

    def totalCount(self):
        """
        Returns the sum of counts for all keys.
        """
        return sum(self.values())

    def normalize(self):
        """
        Edits the counter such that the total count of all
        keys sums to 1.  The ratio of counts for all keys
        will remain the same. Note that normalizing an empty
        Counter will result in an error.
        """
        total = float(self.totalCount())
        if total == 0:
            return
        for key in self.keys():
            self[key] = self[key] / total

    def divideAll(self, divisor):
        """
        Divides all counts by divisor
        """
        divisor = float(divisor)
        for key in self:
            self[key] /= divisor

    def copy(self):
        """
        Returns a copy of the counter
        """
        return Counter(dict.copy(self))

    def __mul__(self, y):
        """
        Multiplying two counters gives the dot product of their vectors where
        each unique label is a vector element.

        >>> a = Counter()
        >>> b = Counter()
        >>> a['first'] = -2
        >>> a['second'] = 4
        >>> b['first'] = 3
        >>> b['second'] = 5
        >>> a['third'] = 1.5
        >>> a['fourth'] = 2.5
        >>> a * b
        14
        """
        sum = 0
        x = self
        if len(x) > len(y):
            x, y = y, x
        for key in x:
            if key not in y:
                continue
            sum += x[key] * y[key]
        return sum

    def __radd__(self, y):
        """
        Adding another counter to a counter increments the current counter
        by the values stored in the second counter.

        >>> a = Counter()
        >>> b = Counter()
        >>> a['first'] = -2
        >>> a['second'] = 4
        >>> b['first'] = 3
        >>> b['third'] = 1
        >>> a += b
        >>> a['first']
        1
        """
        for key, value in y.items():
            self[key] += value

    def __add__(self, y):
        """
        Adding two counters gives a counter with the union of all keys and
        counts of the second added to counts of the first.

        >>> a = Counter()
        >>> b = Counter()
        >>> a['first'] = -2
        >>> a['second'] = 4
        >>> b['first'] = 3
        >>> b['third'] = 1
        >>> (a + b)['first']
        1
        """
        addend = Counter()
        for key in self:
            if key in y:
                addend[key] = self[key] + y[key]
            else:
                addend[key] = self[key]
        for key in y:
            if key in self:
                continue
            addend[key] = y[key]
        return addend

    def __sub__(self, y):
        """
        Subtracting a counter from another gives a counter with the union of all keys and
        counts of the second subtracted from counts of the first.

        >>> a = Counter()
        >>> b = Counter()
        >>> a['first'] = -2
        >>> a['second'] = 4
        >>> b['first'] = 3
        >>> b['third'] = 1
        >>> (a - b)['first']
        -5
        """
        addend = Counter()
        for key in self:
            if key in y:
                addend[key] = self[key] - y[key]
            else:
                addend[key] = self[key]
        for key in y:
            if key in self:
                continue
            addend[key] = -1 * y[key]
        return addend


def raiseNotDefined():
    fileName = inspect.stack()[1][1]
    line = inspect.stack()[1][2]
    method = inspect.stack()[1][3]

    print("*** Method not implemented: %s at line %s of %s" % (method, line, fileName))
    sys.exit(1)


def normalize(vectorOrCounter):
    """
    normalize a vector or counter by dividing each value by the sum of all values
    """
    normalizedCounter = Counter()
    if type(vectorOrCounter) == type(normalizedCounter):
        counter = vectorOrCounter
        total = float(counter.totalCount())
        if total == 0:
            return counter
        for key in counter.keys():
            value = counter[key]
            normalizedCounter[key] = value / total
        return normalizedCounter
    else:
        vector = vectorOrCounter
        s = float(sum(vector))
        if s == 0:
            return vector
        return [el / s for el in vector]


def nSample(distribution, values, n):
    if sum(distribution) != 1:
        distribution = normalize(distribution)
    rand = [random.random() for i in range(n)]
    rand.sort()
    samples = []
    samplePos, distPos, cdf = 0, 0, distribution[0]
    while samplePos < n:
        if rand[samplePos] < cdf:
            samplePos += 1
            samples.append(values[distPos])
        else:
            distPos += 1
            cdf += distribution[distPos]
    return samples


def sample(distribution, values=None):
    if type(distribution) == Counter:
        items = sorted(distribution.items())
        distribution = [i[1] for i in items]
        values = [i[0] for i in items]
    if sum(distribution) != 1:
        distribution = normalize(distribution)
    choice = random.random()
    i, total = 0, distribution[0]
    while choice > total:
        i += 1
        total += distribution[i]
    return values[i]


def sampleFromCounter(ctr):
    items = sorted(ctr.items())
    return sample([v for k, v in items], [k for k, v in items])


def getProbability(value, distribution, values):
    """
      Gives the probability of a value under a discrete distribution
      defined by (distributions, values).
    """
    total = 0.0
    for prob, val in zip(distribution, values):
        if val == value:
            total += prob
    return total


def flipCoin(p):
    r = random.random()
    return r < p


def chooseFromDistribution(distribution):
    "Takes either a counter or a list of (prob, key) pairs and samples"
    if type(distribution) == dict or type(distribution) == Counter:
        return sample(distribution)
    r = random.random()
    base = 0.0
    for prob, element in distribution:
        base += prob
        if r <= base:
            return element


def nearestPoint(pos):
    """
    Finds the nearest grid point to a position (discretizes).
    """
    (current_row, current_col) = pos

    grid_row = int(current_row + 0.5)
    grid_col = int(current_col + 0.5)
    return (grid_row, grid_col)


def sign(x):
    """
    Returns 1 or -1 depending on the sign of x
    """
    if x >= 0:
        return 1
    else:
        return -1


def arrayInvert(array):
    """
    Inverts a matrix stored as a list of lists.
    """
    result = [[] for i in array]
    for outer in array:
        for inner in range(len(outer)):
            result[inner].append(outer[inner])
    return result


def matrixAsList(matrix, value=True):
    """
    Turns a matrix into a list of coordinates matching the specified value
    """
    rows, cols = len(matrix), len(matrix[0])
    cells = []
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == value:
                cells.append((row, col))
    return cells


def lookup(name, namespace):
    """
    Get a method or class from any imported module from its name.
    Usage: lookup(functionName, globals())
    """
    dots = name.count(".")
    if dots > 0:
        moduleName, objName = ".".join(name.split(".")[:-1]), name.split(".")[-1]
        module = __import__(moduleName)
        return getattr(module, objName)
    else:
        modules = [obj for obj in namespace.values() if str(type(obj)) == "<type 'module'>"]
        options = [getattr(module, name) for module in modules if name in dir(module)]
        options += [obj[1] for obj in namespace.items() if obj[0] == name]
        if len(options) == 1:
            return options[0]
        if len(options) > 1:
            raise Exception("Name conflict for %s")
        raise Exception("%s not found as a method or class" % name)


def pause():
    """
    Pauses the output stream awaiting user feedback.
    """
    print("<Press enter/return to continue>")
    input()


# code to handle timeouts
#
# FIXME
# NOTE: TimeoutFuncton is NOT reentrant.  Later timeouts will silently
# disable earlier timeouts.  Could be solved by maintaining a global list
# of active time outs.  Currently, questions which have test cases calling
# this have all student code so wrapped.
#


class TimeoutFunctionException(Exception):
    """Exception to raise on a timeout"""

    pass


class TimeoutFunction:
    def __init__(self, function, timeout):
        self.timeout = timeout
        self.function = function

    def handle_timeout(self, signum, frame):
        raise TimeoutFunctionException()

    def __call__(self, *args, **keyArgs):
        # If we have SIGALRM signal, use it to cause an exception if and
        # when this function runs too long.  Otherwise check the time taken
        # after the method has returned, and throw an exception then.
        if hasattr(signal, "SIGALRM"):
            old = signal.signal(signal.SIGALRM, self.handle_timeout)
            signal.alarm(self.timeout)
            try:
                result = self.function(*args, **keyArgs)
            finally:
                signal.signal(signal.SIGALRM, old)
            signal.alarm(0)
        else:
            startTime = time.time()
            result = self.function(*args, **keyArgs)
            timeElapsed = time.time() - startTime
            if timeElapsed >= self.timeout:
                self.handle_timeout(None, None)
        return result


_ORIGINAL_STDOUT = None
_ORIGINAL_STDERR = None
_MUTED = False


class WritableNull:
    def write(self, string):
        pass


def mutePrint():
    global _ORIGINAL_STDOUT, _ORIGINAL_STDERR, _MUTED
    if _MUTED:
        return
    _MUTED = True

    _ORIGINAL_STDOUT = sys.stdout
    # _ORIGINAL_STDERR = sys.stderr
    sys.stdout = WritableNull()
    # sys.stderr = WritableNull()


def unmutePrint():
    global _ORIGINAL_STDOUT, _ORIGINAL_STDERR, _MUTED
    if not _MUTED:
        return
    _MUTED = False

    sys.stdout = _ORIGINAL_STDOUT
    # sys.stderr = _ORIGINAL_STDERR
