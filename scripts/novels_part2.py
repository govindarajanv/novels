#!/usr/bin/env python3
"""
novels_part2.py — Generates summaries for novels 10 to 17 with strict 100-line validation.
"""

from build_all_summaries import create_summary

def run():
    # 10. At Risk
    create_summary(
        'at-risk', 'At Risk', 'Stella Rimington', 'Espionage / Counter-Terrorism Thriller', '2004',
        'London, MI5 Thames House, Norfolk coastal marshes, Germany',
        [
            ('Liz Carlyle', 'A sharp, dedicated thirty-four-year-old intelligence officer in MI5’s Counter-Espionage branch.'),
            ('Charles Wetherby', 'Liz’s calm, experienced MI5 section director and trusted professional mentor.'),
            ('Bruno McKay', 'A charismatic, ambitious MI6 liaison officer navigating inter-agency territorial friction.'),
            ('Fariba', 'A British-Pakistani community asset providing critical street-level counter-terror intelligence.'),
            ('The Invisible', 'A radicalized British passport holder recruited abroad to conduct undetected domestic strikes.'),
            ('Peggy', 'Liz’s perceptive, gardening mother who provides a grounded emotional anchor outside Thames House.'),
            ('Mark Green', 'A veteran Special Branch police commander leading tactical counter-terror surveillance squads.'),
            ('Carl Kramer', 'A seasoned German intelligence handler tracking Middle Eastern extremist logistics networks.')
        ],
        ('Intelligence Alert & The Invisible', [
            'A classified intelligence cable from German intelligence lands on Liz Carlyle’s desk at MI5 headquarters in London.',
            'The alert warns that an extremist cell is preparing to infiltrate the United Kingdom with an \'invisible\' operative.',
            'In intelligence parlance, an invisible is a British citizen with no criminal record or surveillance flag, capable of moving undetected.',
            'Liz’s director Charles Wetherby establishes an emergency joint task force with MI6 foreign intelligence and Special Branch.',
            'Liz is tasked with identifying the sleeper agent before the unknown domestic target can be selected and struck.',
            'Pressure mounts as Downing Street demands immediate containment without triggering public panic or civil unrest.'
        ]),
        ('Inter-Agency Intrigue & Covert Leads', [
            'Liz liaises with MI6 officer Bruno McKay, encountering bureaucratic posturing and mutual suspicion between domestic and foreign services.',
            'While MI6 focuses on overseas satellite intercepts and foreign camps, Liz concentrates on clandestine domestic support networks.',
            'She meets with trusted field asset Fariba, who reports rumors of a radicalized English convert returning from the Balkans.',
            'Electronic wiretaps and financial tracing flag unusual cash disbursements originating from front charities in Hamburg.',
            'Special Branch commander Mark Green initiates discreet photographic surveillance on suspected transit safe houses across London.',
            'Liz works seventy-hour weeks, sleeping on her office sofa while balancing concerns for her aging mother Peggy.',
            'A crucial clue emerges: a maritime supply requisition linking a coastal Norfolk fishing vessel to the Hamburg network.'
        ]),
        ('Surveillance Along the Norfolk Coast', [
            'Liz deploys a mobile surveillance unit to the isolated, fog-shrouded salt marshes of the North Norfolk coastline.',
            'They track a suspicious skipper meeting a foreign courier in a desolate pub near the Blakeney tidal estuaries.',
            'Through thermal imaging and listening bugs, the team observes the arrival of an athletic young man traveling under a forged passport.',
            'The operative is identified as an English-born convert with advanced tactical training in weapons and chemical synthesis.',
            'Liz realizes the terrorist does not fit traditional intelligence profiles, allowing him to blend seamlessly into civilian crowds.',
            'A tactical debate erupts: MI6 urges an immediate armed arrest, while Liz insists on shadowing him to uncover his intended target.',
            'Wetherby backs Liz’s judgment, authorizing an intense twenty-four-hour tracking operation as the operative heads toward London.'
        ]),
        ('The Target Revealed & Clock Ticking', [
            'The operative rents an anonymous lock-up garage on the outskirts of London, stocking industrial fertilizer and detonator cord.',
            'Liz’s intelligence analysts intercept encrypted radio signals detailing an impending strike against a high-profile diplomatic summit.',
            'British, American, and Middle Eastern peace delegates are scheduled to convene at a historic government conference estate.',
            'The terrorist plans to deploy a devastating truck bomb into the secure motorcade perimeter during the opening ceremonies.',
            'Special Branch snipers and elite SAS counter-terror teams are placed on maximum alert across the Greater London area.',
            'The operative detects tailing surveillance vehicles, executing a brilliant evasive maneuver and disappearing into the London commuter grid.',
            'Panic grips Thames House as the countdown to the diplomatic summit narrows to less than twelve hours.'
        ]),
        ('The Tactical Showdown', [
            'Refusing to succumb to hysteria, Liz retraces the suspect’s logistical footprint, calculating his probable backup launch site.',
            'She deduces that the vehicle was loaded and pre-staged in an abandoned commercial transport depot near the conference route.',
            'Liz and Special Branch units converge on the depot just as the armed operative starts the explosive-laden delivery van.',
            'A violent exchange of gunfire breaks out across the concrete loading docks as the terrorist attempts to ram the exit gate.',
            'Mark Green’s tactical marksmen disable the vehicle’s tires, while Liz coordinates the perimeter lockdown to prevent civilian casualties.',
            'The cornered extremist attempts to manually detonate the explosive charge from the cab using a hardwired switch.',
            'A sniper neutralizes the operative seconds before detonation, allowing bomb disposal experts to disarm the massive chemical device.',
            'Liz exhales in profound relief, having averted what would have been the deadliest terror attack in modern British history.'
        ]),
        ('Aftermath & The Shadow War', [
            'Thames House quietly celebrates the operation’s triumph, though official secrecy prevents any public recognition of Liz’s heroism.',
            'Prime ministerial commendations are delivered behind closed doors, while inter-agency rivalries briefly give way to respect.',
            'Bruno McKay acknowledges Liz’s superior investigative acumen, establishing a mutual professional truce.',
            'Liz reflects upon the harrowing modern landscape of asymmetric warfare, where domestic citizens turn against their own society.',
            'She returns home to Norfolk for a quiet weekend with her mother, seeking restoration in the unhurried rhythms of the garden.',
            'Yet the hum of her encrypted secure phone reminds her that the defense of the realm never truly ceases.',
            'Liz returns to London on Monday morning, ready to confront the next shadow threat lurking beyond the horizon.',
            'The novel closes on an authentic, grounded portrait of modern professional intelligence service dedicated to civilian safety.'
        ]),
        [
            ('Authenticity of Modern Espionage', 'Leverages former MI5 Director General Stella Rimington’s firsthand authority to depict procedural tradecraft accurately.'),
            ('The Evolution of Terrorism', 'Explores the complex, unsettling phenomenon of home-grown extremism and clean-skin operatives operating within modern borders.'),
            ('Institutional Friction & Collaboration', 'Deconstructs the pragmatic tensions, rivalry, and vital synergy between domestic (MI5) and foreign (MI6) services.'),
            ('A Pioneering Heroine', 'Introduces Liz Carlyle as a compelling, realistic, and unglamorous female intelligence protagonist for the post-9/11 era.')
        ]
    )

    # 11. The No.1 Ladies' Detective Agency
    create_summary(
        'the-no-1-ladies-detective-agency', "The No.1 Ladies' Detective Agency", 'Alexander McCall Smith', 'Gentle Mystery / Cultural Fiction', '1998',
        'Gaborone, Mochudi, and the Kalahari Desert plains of Botswana, Southern Africa',
        [
            ('Precious Ramotswe', 'A wise, intuitive, traditionally built Motswana woman who founds Botswana’s first female private detective agency.'),
            ('Obed Ramotswe', 'Precious’s late, revered father whose cattle legacy and ethical wisdom guide her moral worldview.'),
            ('Grace Makutsi', 'Precious’s brilliant, fiercely loyal secretary from the Botswana Secretarial College with a legendary 97% exam score.'),
            ('Mr. J.L.B. Matekoni', 'The kind, honorable proprietor of Tlokweng Road Speedy Motors who loves Precious and aids her investigations.'),
            ('Note Mokoti', 'Precious’s charismatic but abusive jazz-trumpeter ex-husband whose cruelty forged her fierce independence.'),
            ('Happy Bapetsi', 'A hard-working, devoted client who suspects that a man claiming to be her long-lost father is a ruthless imposter.'),
            ('Dr. Charles Komoti', 'A wealthy, secretive physician whose suspicious medical malpractice and erratic schedules arouse client alarm.'),
            ('The Witch Doctor', 'A sinister rural traditional practitioner implicated in the abduction of young children for muti medicine.')
        ],
        ('A Daughter of Africa Sets Up Shop', [
            'Following the death of her beloved father Obed, Precious Ramotswe inherits a valuable herd of cattle in rural Mochudi.',
            'Rather than investing in conventional enterprises, Precious sells the livestock and moves to the capital city of Gaborone.',
            'At the foot of Kgale Hill, she purchases a modest building and founds the No. 1 Ladies’ Detective Agency, the first in Botswana.',
            'Armed with a battered white van, a teapot of red rooibos tea, and profound insight into human nature, she opens for business.',
            'She hires Grace Makutsi, a proud, impoverished graduate of the Botswana Secretarial College who scored ninety-seven percent.',
            'Precious vows to help people with the problems of their lives, applying patience, kindness, and traditional African morality.'
        ]),
        ('Cases of Fraud & The Bogus Father', [
            'Her first client is Happy Bapetsi, a hardworking accountant whose peaceful home is invaded by a stranger claiming to be her father.',
            'The man demands financial support, free meals, and lodging, exploiting African traditions of filial obligation.',
            'Precious investigates with subtle cunning, discreetly orchestrating a medical bone-setting test that exposes the man as a fraudulent parasite.',
            'Delighted with the respectful resolution, Happy pays handsomely and recommends the agency across Gaborone.',
            'Another client hires Precious to investigate a local witch doctor whose expensive fertility charms are causing severe distress.',
            'Precious also unmasks an unfaithful husband by deploying clever surveillance, comforting the betrayed wife with warm tea and dignity.',
            'Her kind neighbor, mechanic Mr. J.L.B. Matekoni, watches Precious with growing admiration, frequently repairing her tiny white van.'
        ]),
        ('The Mysterious Vanishing of Thobiso', [
            'A deeply anguished client, a respected schoolteacher, consults Precious regarding the disappearance of her eleven-year-old son Thobiso.',
            'Ten years earlier, the young boy vanished from his village; local whispers suggest he was kidnapped for traditional muti medicine.',
            'Muti involves ritual sacrifices orchestrated by unscrupulous witch doctors seeking potent charms for wealthy clients.',
            'The police abandoned the cold case long ago, but Precious feels an overwhelming maternal imperative to seek the truth.',
            'Precious recalls her own tragic past: giving birth to a premature infant who lived only five days during her abusive marriage to Note Mokoti.',
            'That profound loss fuels her sacred commitment to protect children and heal grieving mothers across her homeland.',
            'Precious begins scouring remote cattle-posts along the fringes of the vast Kalahari Desert for traces of the lost youth.'
        ]),
        ('Confronting the Witch Doctor’s Wife', [
            'Through patient inquiries and discreet conversations over bush tea, Precious identifies a wealthy Gaborone merchant seeking luck.',
            'The merchant frequently visited an isolated, feared traditional healer living in a remote compound near the Molopolole road.',
            'Precious drives her white van into the wilderness to interview the witch doctor’s estranged, guilt-ridden wife.',
            'Fearing divine retribution and sensing Precious’s deep goodness, the woman breaks down in tears and makes a horrifying confession.',
            'She reveals that her husband did not kill young Thobiso, but sold him into captive servitude at an isolated cattle-post.',
            'The boy has spent a decade trapped as a virtual slave, herding cattle in complete isolation from the outside world.',
            'Armed with the remote post’s coordinates, Precious prepares for a perilous rescue expedition into the Kalahari plains.'
        ]),
        ('The Kalahari Rescue & Liberation', [
            'Precious navigates deep sandy ruts and thorny acacia scrublands, locating the desolate cattle-post far beyond cell coverage.',
            'She discovers Thobiso living in a crude mud shelter, barefoot, illiterate, and terrified, guarding cattle under harsh conditions.',
            'Precious gently approaches the traumatized youth, speaking in his mother tongue and assuring him that his family never stopped searching.',
            'She feeds him warm food, wraps him in a blanket, and drives him safely back across the desert to Gaborone.',
            'The reunion between the weeping mother and her long-lost son is a radiant moment of profound communal joy and tears.',
            'Precious coordinates with trusted police contacts to ensure the corrupt witch doctor and his network are permanently dismantled.',
            'News of the extraordinary rescue cements Precious’s status as a revered heroine of justice and compassion throughout Botswana.',
            'Yet Precious remains utterly humble, insisting that she merely did what any good daughter of Africa would do.'
        ]),
        ('Partnership, Romance & Peace', [
            'The emotional intensity of the case brings Precious and Mr. J.L.B. Matekoni closer together in profound mutual tenderness.',
            'Recognizing his steadfast loyalty, gentle kindness, and deep goodness, Precious accepts his heartfelt proposal of marriage.',
            'Grace Makutsi receives a well-deserved promotion to assistant detective, celebrated with a new pair of spectacles and tea.',
            'Together, Precious and Mr. J.L.B. Matekoni prepare to foster two orphaned children, opening their hearts to a joyful future.',
            'Precious sits on her porch in the golden African sunset, listening to the crickets and sipping hot red bush tea.',
            'She reflects upon the enduring wisdom of her father Obed and the beauty of Botswana, a land of peace, cattle, and love.',
            'The novel closes on an uplifting, luminous tribute to kindness, moral clarity, and the quiet triumph of the human spirit.',
            'Under the vast Southern Cross stars, Precious Ramotswe smiles, ready to face whatever tomorrow brings with grace.'
        ]),
        [
            ('Traditional Morality & Decency', 'Celebrates the enduring Botswana ethic of *Botho*—mutual respect, human dignity, and communal harmony.'),
            ('Gentle Wisdom over Violence', 'Subverts hardboiled detective tropes by prioritizing empathy, psychological intuition, and dialogue over physical brutality.'),
            ('A Vibrant African Tapestry', 'Presents a radiant, affectionate portrait of post-colonial Botswana, highlighting its peace, democracy, and cultural beauty.'),
            ('Global Phenomenon', 'Alexander McCall Smith’s beloved international bestseller spawned an iconic multi-volume literary series.')
        ]
    )

    # 12. The Da Vinci Code
    create_summary(
        'the-da-vinci-code', 'The Da Vinci Code', 'Dan Brown', 'Conspiracy Thriller / Mystery', '2003',
        'Paris, Louvre Museum, Château de Villette, London, Temple Church, Westminster Abbey, Rosslyn Chapel Scotland',
        [
            ('Robert Langdon', 'A Harvard University professor of religious symbology caught in an international murder conspiracy.'),
            ('Sophie Neveu', 'A gifted French police cryptographer who discovers she is the guardian of an ancient dynastic lineage.'),
            ('Jacques Saunière', 'The revered Louvre curator and Grand Master of the Priory of Sion whose murder initiates the quest.'),
            ('Sir Leigh Teabing', 'A wealthy, eccentric British historian and Grail scholar secretly operating as the conspiratorial Teacher.'),
            ('Silas', 'A devout, albino Opus Dei monk manipulated into committing assassinations under religious zealotry.'),
            ('Captain Bezu Fache', 'The tenacious, bulldog-like director of the French Judicial Police pursuing Langdon as the prime suspect.'),
            ('Bishop Manuel Aringarosa', 'The head of Opus Dei seeking to protect his traditionalist prelature from Vatican marginalization.'),
            ('André Vernet', 'The refined manager of the Zurich Depository Bank in Paris who assists Langdon and Sophie’s escape.')
        ],
        ('Murder in the Louvre', [
            'Louvre curator Jacques Saunière is mortally wounded by an assassin inside the Grand Gallery of the world-famous Paris museum.',
            'Before dying, Saunière strips naked, positions his corpse like Da Vinci’s Vitruvian Man, and inscribes cryptic anagrams in invisible marker.',
            'Harvard symbologist Robert Langdon, in Paris delivering a lecture on pagan iconography, is summoned to the crime scene.',
            'French police captain Bezu Fache suspects Langdon of the murder, as Saunière wrote \'P.S. Find Robert Langdon\' on the parquet floor.',
            'Police cryptographer Sophie Neveu arrives, warning Langdon that Fache planted a GPS tracker in his pocket to engineer his arrest.',
            'Sophie reveals that the \'P.S.\' refers to Princess Sophie—her childhood nickname—and that Saunière was her estranged grandfather.'
        ]),
        ('The Cryptex & Flight from Paris', [
            'Sophie helps Langdon stage a daring escape from the Louvre by tossing the tracking beacon onto a passing transport truck.',
            'They decipher Saunière’s anagrams, which lead them to Leonardo da Vinci’s *Mona Lisa* and *Madonna of the Rocks*.',
            'Hidden behind the painting’s protective glass, they discover an antique wooden key inscribed with a Swiss banking address.',
            'Evading police cordons, Langdon and Sophie reach the Zurich Depository Bank and unlock a secure automated safe deposit vault.',
            'Inside sits an exquisite rosewood box containing a cryptex, a portable puzzle cylinder invented by Da Vinci to protect parchment scrolls.',
            'If forced open without the secret five-letter password, a delicate glass vial of vinegar breaks, dissolving the papyrus within.',
            'Bank manager André Vernet aids their escape in an armored van before attempting to double-cross them, forcing them to flee.'
        ]),
        ('Château de Villette & The Secret History', [
            'Seeking scholarly sanctuary, Langdon and Sophie arrive at Château de Villette, the magnificent estate of Sir Leigh Teabing.',
            'Teabing, a lifelong Holy Grail obsessive, reveals the revolutionary thesis of the clandestine brotherhood known as the Priory of Sion.',
            'He explains that the Holy Grail is not an earthly chalice, but Mary Magdalene, the royal wife and mother of Jesus Christ’s children.',
            'Da Vinci encoded this secret in *The Last Supper*, painting Magdalene to the right of Christ rather than the apostle John.',
            'Silas, the albino monk acting on orders from a shadowy mastermind called \'The Teacher\', infiltrates the château to steal the cryptex.',
            'Langdon and Teabing overpower Silas, binding him and fleeing aboard Teabing’s private Hawker aircraft bound for England.',
            'Fache pursues them across international airspace, alerting British authorities to intercept the fugitive aircraft in London.'
        ]),
        ('The London Pursuit & The Teacher Exposed', [
            'Landing covertly in Kent, Teabing, Langdon, and Sophie slip through police checkpoints and travel directly into central London.',
            'They visit the ancient Temple Church to inspect the tombs of the Knights Templar, searching for the cryptex’s unlocking clue.',
            'Silas escapes his bonds with assistance from Teabing’s treacherous manservant Rémy, seizing the cryptex and abducting Teabing.',
            'Rémy is poisoned with peanut dust by The Teacher, who is shockingly revealed to be none other than Sir Leigh Teabing himself.',
            'Teabing orchestrated Saunière’s murder to force the Priory to reveal the hidden Grail documents to the public before his death.',
            'Silas realizes he was tragically manipulated, engaging police in a panicked shootout outside Opus Dei headquarters and dying of wounds.',
            'Teabing corners Langdon and Sophie inside Westminster Abbey at the tomb of Sir Isaac Newton, demanding the cryptex password.'
        ]),
        ('Climax at Newton’s Tomb', [
            'Standing beneath the towering monuments of Westminster Abbey, Teabing holds Langdon and Sophie at gunpoint.',
            'Teabing explains that Newton was a Priory Grand Master and that the missing orb upon his tomb holds the secret password.',
            'Langdon realizes the orb refers not to celestial bodies, but to the mythical falling apple that unlocked gravitational physics.',
            'Feigning failure, Langdon tosses the cryptex into the high vaulting ceiling; Teabing drops his firearm to catch the falling cylinder.',
            'The cryptex smashes on the stone floor, but Langdon opens his palm to reveal he had already entered the password \'APPLE\'.',
            'He extracted the inner parchment safe and intact; Captain Fache bursts into the abbey with armed police, arresting Teabing.',
            'Armed tactical units escort the shouting Teabing into custody as shocked tourists gaze at the scene.',
            'Fache apologizes to Langdon and clears him of all charges, having discovered Teabing’s audio bugging equipment at the château.'
        ]),
        ('Rosslyn Chapel & The Sacred Feminine', [
            'The final papyrus riddle guides Langdon and Sophie north across the border into Scotland to the enigmatic Rosslyn Chapel.',
            'Beneath the gothic stone carvings, they discover no physical tomb, but meet the chapel’s curator, an elderly French woman.',
            'The curator is revealed to be Saunière’s widow, and Sophie discovers that she and her surviving brother are direct Merovingian descendants.',
            'Sophie is reunited with her grandmother and heritage, realizing why Saunière sacrificed his life to protect her identity.',
            'Langdon returns to Paris, waking at dawn to follow the historic Rose Line brass medallions embedded across the city streets.',
            'The trail leads him beneath the glass Inverted Pyramid at the Louvre, where the sarcophagus of Mary Magdalene rests beneath stone.',
            'Langdon kneels in reverent wonder beneath the starry Parisian sky, humbled by the enduring power of the sacred feminine.',
            'The novel closes on a transcendent image of ancient truth preserved in silence beneath the heart of human civilization.'
        ]),
        [
            ('The Sacred Feminine', 'Popularized alternative theological narratives regarding Mary Magdalene, feminine spiritual power, and forgotten histories.'),
            ('The Power of Symbols and Codes', 'Celebrates the thrilling intellectual puzzles of cryptology, art history, architecture, and sacred geometry.'),
            ('Institutional Secrecy vs. Truth', 'Dramatizes the historical clashes between orthodox religious authorities and secret societies preserving forbidden knowledge.'),
            ('Cultural Juggernaut', 'Became one of the bestselling novels of all time, sparking global debates, documentaries, and Hollywood adaptations.')
        ]
    )

    # 13. Up and Down in the Dales
    create_summary(
        'up-and-down-in-the-dales', 'Up and Down in the Dales', 'Gervase Phinn', 'Memoir / Humorous Pastoral Nonfiction', '2004',
        'Yorkshire Dales, North Yorkshire, England, rural stone hamlets and village schools',
        [
            ('Gervase Phinn', 'A genial, perceptive, and deeply compassionate school inspector traveling through the Yorkshire Dales.'),
            ('Christine Phinn', 'Gervase’s loving, pragmatic wife who grounds his whimsical nature with affection and humor.'),
            ('Harold Sugden', 'The crusty, formidable Chief Inspector of Schools whose bark is far worse than his benevolent bite.'),
            ('Connie', 'The omniscient County Hall secretary who manages department politics, tea supplies, and administrative secrets.'),
            ('Sister Brenda', 'A formidable, razor-sharp Catholic headmistress whose strict discipline masks an immense maternal heart.'),
            ('Mrs. Savage', 'An eccentric, commanding village primary headteacher who manages her hillside school like a royal court.'),
            ('Jack Fawcett', 'A shrewd, plain-spoken Dales farmer and school governor whose rustic wisdom outsmarts city bureaucrats.'),
            ('Mary', 'Gervase’s warm, traditional mother whose nostalgic Yorkshire stories inspire his enduring love for education.')
        ],
        ('A School Inspector in the Hills', [
            'Gervase Phinn embarks upon another vibrant school term as County School Inspector across the breathtaking Yorkshire Dales.',
            'Driving his trusty car along winding limestone lanes, Gervase navigates drystone walls, grazing sheep, and sudden dales gales.',
            'His mission is not bureaucratic policing, but nurturing teachers, celebrating childhood imagination, and ensuring rural educational excellence.',
            'At County Hall in Northallerton, senior inspector Harold Sugden rumbles about budgets, while cheerful secretary Connie dispenses tea and gossip.',
            'Gervase treasures his home life with his supportive wife Christine, whose impending motherhood brings joy to their stone cottage.',
            'Setting out across Swaledale and Wensleydale, Gervase anticipates another season of hilarious misunderstandings and tender human triumphs.'
        ]),
        ('The Wisdom and Wit of Dales Children', [
            'Visiting a remote hillside school, Gervase sits on miniature wooden chairs, listening to five-year-olds read aloud from storybooks.',
            'When examining a reading class, a serious little boy solemnly explains that \'an adult is somebody who has stopped growing at both ends\'.',
            'Another pupil, asked to recite the Lord’s Prayer, confidently declares: \'Our Father, which art in heaven, Harold be thy name!\'',
            'Gervase marvels at the innocent literalism of rural children, recording their candid observations in his leather inspection notebook.',
            'During a nature walk, children introduce him to local dialect terms for insects, weather phenomena, and wild hillside plants.',
            'Gervase defends creative teaching against rigid testing mandates, encouraging teachers to let children write poetry inspired by the moors.',
            'The pure delight of discovery among Dales pupils reaffirms Gervase’s profound calling as an educator of the heart.'
        ]),
        ('Eccentric Heads & Village Politics', [
            'At St. Jude’s Catholic Primary, Gervase is welcomed by the formidable Sister Brenda, who rules her school with iron grace.',
            'Sister Brenda effortlessly tames unruly classroom boys while feeding Gervase homemade fruitcake and sharp educational philosophy.',
            'At another tiny one-room schoolhouse, Mrs. Savage greets Gervase dressed in full tweed regalia with three barking terriers.',
            'Mrs. Savage insists that before inspecting arithmetic, Gervase must taste her elderberry wine and judge the autumn vegetable show.',
            'Gervase attends a village school governors’ meeting in a drafty church hall, presided over by shrewd sheep farmer Jack Fawcett.',
            'When a slick regional official proposes closing the small school for efficiency, Fawcett demolishes the bureaucrat with earthy Dales logic.',
            'The school remains open, celebrated with mugs of strong tea and mutual congratulations among the villagers.'
        ]),
        ('Winter Storms & Rural Solidarity', [
            'A fierce winter blizzard descends upon the Dales, burying stone hamlets and rural schoolyards under towering snowdrifts.',
            'Gervase’s vehicle becomes hopelessly stranded in a snowdrift near a remote high-moor farmstead in Wharfedale.',
            'Local farmers arrive with tractors and shovels, digging out his vehicle without hesitation and inviting him in for hot broth.',
            'Stranded at a village school overnight, Gervase and the local headteacher keep thirty pupils warm with roaring fires and storytelling.',
            'The children sing traditional Yorkshire folk songs by candlelight, transforming a perilous storm into an enchanting holiday adventure.',
            'Gervase witnesses the extraordinary resilience and community solidarity that define life in isolated mountain farming valleys.',
            'The deep human bonds forged amidst winter hardships showcase the enduring strength of traditional English country life.'
        ]),
        ('Triumph at the Speech Festival', [
            'Spring arrives, covering the emerald Dales meadows in bright yellow daffodils and thousands of gamboling lambs.',
            'Gervase coordinates the annual Dales Schools Speech and Drama Festival, bringing together hundreds of rural children to perform.',
            'Nervous village pupils recite Shakespeare, traditional dialects, and original poetry with breathtaking sincerity and passion.',
            'A painfully shy boy from a remote fell farm steps onto the stage, captivating the entire auditorium with an exquisite poem about his sheepdog.',
            'Harold Sugden dabs a tear from his eye, gruffly praising Gervase for organizing an event that honors rural talent.',
            'The festival concludes with standing ovations, golden certificates, and beaming parents filling the market town hall with cheers.',
            'Village elders and local shopkeepers celebrate the children’s triumphs late into the warm spring evening at the parish hall.',
            'For Gervase, witnessing children discover their voices is the supreme reward of his educational pilgrimage.'
        ]),
        ('A New Generation in the Dales', [
            'Christine goes into labor on a golden midsummer evening, and Gervase races to the hospital in Northallerton with racing pulse.',
            'He welcomes their newborn child into the world, overwhelmed with awe, gratitude, and a profound sense of life coming full circle.',
            'Colleagues, headteachers, and Dales farmers flood their cottage with handwritten letters, knitted baby woolens, and jars of wild honey.',
            'Holding his baby at the cottage window, Gervase gazes out over the rolling limestone fells glowing in the twilight.',
            'He reflects upon the humor, wisdom, eccentricities, and enduring kindness of the people who call the Yorkshire Dales home.',
            'He realizes that true education is not found in regulatory checklists, but in love, laughter, and community fellowship.',
            'The memoir concludes with joyful hope, gratitude for family, and a celebratory toast to the incomparable beauty of Yorkshire.',
            'Gervase prepares his inspection briefcase for another term, ready to travel up and down the beloved dales for years to come.'
        ]),
        [
            ('The Joy of Primary Education', 'Celebrates the purity, wonder, and humor of childhood imagination nurtured by dedicated rural schoolteachers.'),
            ('A Vanishing Rural Tapestry', 'Preserves the distinct dialects, eccentric personalities, and close-knit solidarity of traditional Yorkshire communities.'),
            ('Compassionate Bureaucracy', 'Advocates for human-centered educational leadership that values artistic creativity and joy over cold standardized testing.'),
            ('Beloved English Voice', 'Dubbed the \'James Herriot of schools\', Gervase Phinn delivers a bestselling, warmhearted masterpiece of British pastoral humor.')
        ]
    )

    # 14. The Return of the Dancing Master
    create_summary(
        'the-return-of-the-dancing-master', 'The Return of the Dancing Master', 'Henning Mankell', 'Nordic Noir / Historical Mystery', '2000',
        'Härjedalen forests, Sveg, Borås, Sweden, with flashbacks to WWII Germany and post-war Argentina',
        [
            ('Stefan Lindman', 'A thoughtful thirty-seven-year-old Swedish police detective struggling with a devastating diagnosis of mouth cancer.'),
            ('Herbert Molin', 'A reclusive retired police officer brutally tortured and executed in his isolated northern cabin.'),
            ('Giuseppe Larsson', 'The weary, methodical local police inspector in Sveg heading the gruesome Molin homicide inquiry.'),
            ('Abraham Andersson', 'Molin’s elderly rural neighbor who is murdered while clearing snow after spotting suspicious visitors.'),
            ('Vera Lind', 'An enigmatic local woman whose family history is deeply entwined with Swedish wartime Nazi sympathizers.'),
            ('Fernando Molin', 'Molin’s son residing in South America, preserving his father’s violent ideological connections.'),
            ('Elena', 'A Swedish state security intelligence analyst investigating clandestine far-right underground networks.'),
            ('The Executioner', 'A shadowy, relentless figure hunting down surviving perpetrators of World War II war crimes.')
        ],
        ('A Gruesome Murder in the Snow', [
            'In the dark, freezing forests of northern Sweden’s Härjedalen province, retired policeman Herbert Molin lives in total isolation.',
            'Molin is discovered dead inside his remote cabin, having been subjected to sadistic, ritualistic flogging and execution.',
            'Chillingly, the killer left bloody footprints on the hardwood floorboards arranged in the intricate steps of the Argentine tango.',
            'In Borås, detective Stefan Lindman receives the shocking news while grappling with a diagnosis of malignant tongue cancer.',
            'Molin had been Stefan’s former police colleague and mentor years earlier before abruptly retreating into northern reclusiveness.',
            'Terrified of his impending medical treatments and facing mortality, Stefan takes medical leave and drives north to Sveg.'
        ]),
        ('The Shadows of Sveg', [
            'Stefan arrives in the snowbound town of Sveg, discreetly conducting private inquiries alongside official police investigator Giuseppe Larsson.',
            'Stefan inspects Molin’s bloodstained cabin, disturbed by the victim’s obsessive perimeter defenses and armed guard dogs.',
            'Hidden inside a locked wall cavity, Stefan uncovers photographs, diaries, and Nazi medals dating back to World War II.',
            'The respected Swedish policeman was secretly a volunteer officer in the Waffen-SS, participating in brutal atrocities on the Eastern Front.',
            'Molin escaped postwar prosecution through ratline networks, spending decades hiding in Argentina before returning to Sweden.',
            'The mysterious tango footprints on the floor represented the dance steps Molin forced death camp prisoners to perform before execution.',
            'Stefan is sickened by the realization that his former police mentor was an unrepentant, sadistic war criminal.'
        ]),
        ('A Second Execution in the Forest', [
            'While the police canvas local logging roads, Molin’s elderly neighbor Abraham Andersson is shot dead on his driveway.',
            'The killer used a high-powered hunting rifle, executing Andersson while the old man was clearing snow with his snowblower.',
            'Stefan deduces that Andersson was murdered because he accidentally witnessed the killer arriving at Molin’s property.',
            'Stefan’s private inquiries attract dangerous attention; his hotel room is ransacked, and threatening notes are slipped under his door.',
            'Stefan begins experiencing severe physical pain from his cancer, relying on painkillers while relentlessly pursuing the truth.',
            'He discovers that a covert network of wealthy Swedish Nazi sympathizers has been operating undisturbed since 1945.',
            'Funded by expatriates in Argentina, the underground network has been grooming militant neo-Nazi youth for modern domestic terrorism.'
        ]),
        ('The Argentine Connection & Neo-Nazi Terror', [
            'Stefan connects with state security analyst Elena, cross-referencing Molin’s financial assets with overseas wire transfers.',
            'Molin’s son Fernando coordinates international funding for extreme right-wing cells operating in Stockholm and Malmö.',
            'Stefan interviews local resident Vera Lind, discovering that her late father was Molin’s comrade in wartime SS divisions.',
            'Vera reveals that Molin lived in terror during his final months, convinced that an old enemy had tracked him from South America.',
            'Stefan tracks a suspicious vehicle to a secluded lodge, where young neo-Nazi militants are conducting paramilitary firearms training.',
            'Stefan is ambushed in the woods, narrowly escaping execution by throwing himself into an icy river gorge in pitch darkness.',
            'Hypothermic and injured, Stefan crawls to a rural roadway, rescued by a snowplow operator and hospitalized under police guard.'
        ]),
        ('The Executioner Unmasked', [
            'Refusing to remain bedridden, Stefan discharges himself to confront the mastermind behind the tango executions.',
            'He identifies the killer not as a neo-Nazi terrorist, but as an elderly Jewish survivor whose family was slaughtered by Molin.',
            'Having tracked Molin across continents for over fifty years, the avenger meticulously reconstructed the tango ritual for judgment.',
            'Stefan tracks the executioner to an abandoned railway warehouse near the Norwegian border as the avenger prepares to leave Sweden.',
            'A tense, heartbreaking psychological confrontation unfolds between the dying detective and the vengeful survivor.',
            'The executioner explains that when lawful institutions fail to punish genocide, survivors are left with only memory and vengeance.',
            'Before police units can breach the perimeter, the executioner chooses suicide, refusing to surrender to Swedish judicial custody.',
            'Stefan stands over the scene in heavy silence, overwhelmed by the tragic, inescapable vortex of twentieth-century history.'
        ]),
        ('Acceptance, Justice & The Will to Live', [
            'Swedish security forces raid the clandestine neo-Nazi compound, arresting militant operatives and dismantling international funding conduits.',
            'Giuseppe Larsson thanks Stefan for his brilliant investigative contributions, clearing the official homicide files in Sveg.',
            'Stefan returns home to Borås, fundamentally altered by his journey through the darkest recesses of human evil.',
            'Confronting the terrifying legacy of hatred helps Stefan put his personal battle with cancer into perspective.',
            'He decides to stop running from medical intervention, courageously checking into the oncology clinic to undergo surgery.',
            'Surrounded by medical staff and supportive friends, Stefan feels an overwhelming, resilient determination to survive.',
            'He understands that while evil persists across generations, the fight for justice and human dignity must never be abandoned.',
            'The novel closes on Stefan Lindman stepping toward the operating theater with quiet courage, choosing life over despair.'
        ]),
        [
            ('The Lingering Cancer of Nazism', 'Exposes Sweden’s uncomfortable historical wartime neutrality and the persistent underground presence of neo-fascist networks.'),
            ('Justice vs. Private Retribution', 'Explores the agonizing moral dilemmas of hunting unpunished war criminals when official legal avenues have failed.'),
            ('Mortality & The Human Condition', 'Weaves the protagonist’s existential battle with throat cancer into a powerful meditation on vulnerability and resilience.'),
            ('Masterful Nordic Noir', 'Henning Mankell delivers a chilling, brooding masterpiece of atmospheric psychological suspense and historical reckoning.')
        ]
    )

    # 15. A Gathering Light
    create_summary(
        'a-gathering-light', 'A Gathering Light', 'Jennifer Donnelly', 'Historical Fiction / Coming-of-Age Bildungsroman', '2003',
        'Adirondack Mountains, Eagle Bay, Big Moose Lake, Herkimer County, New York, summer 1906',
        [
            ('Mattie Gokey', 'A gifted, fiercely intelligent sixteen-year-old girl torn between family duty and her dream of becoming a writer.'),
            ('Grace Brown', 'A poignant, pregnant factory worker whose desperate love letters uncover a tragic murder plot.'),
            ('Chester Gillette', 'Grace’s handsome, socially ambitious lover who murders her on Big Moose Lake to protect his reputation.'),
            ('Weaver Smith', 'Mattie’s brilliant African-American classmate who endures vicious racial prejudice to pursue college.'),
            ('Pa (Mr. Gokey)', 'Mattie’s harsh, grief-stricken widowed father whose farm poverty traps his family in unrelenting toil.'),
            ('Miss Wilcox', 'Mattie’s inspirational high-school teacher who secretly publishes radical feminist poetry under a pseudonym.'),
            ('Royal Loomis', 'A handsome, traditional local farmer who proposes marriage to Mattie, offering security at the cost of her soul.'),
            ('Minnie Compeau', 'Mattie’s vivacious, free-spirited best friend whose early pregnancy exposes the brutal traps of rural womanhood.')
        ],
        ('A Promise in the Dust', [
            'In the rugged Adirondack mountains in 1906, sixteen-year-old Mattie Gokey struggles against crushing rural poverty.',
            'Following her mother’s agonizing death from cancer, Mattie promised on her deathbed to stay and raise her three younger sisters.',
            'Her father Pa is an embittered, exhausted farmer who views books, literature, and college aspirations as wasteful vanity.',
            'Mattie possesses extraordinary literary talent, secretly collecting words in a dictionary and writing essays by candle stub.',
            'Her teacher Miss Wilcox recognizes Mattie’s genius, helping her earn a scholarship to prestigious Barnard College in New York City.',
            'Torn between filial duty to her family and her passionate hunger for an intellectual life, Mattie’s heart is deeply divided.'
        ]),
        ('The Glenmore Hotel & The Secret Letters', [
            'To earn thirty dollars for her family’s farm taxes, Mattie takes a summer job as a kitchen maid at the luxurious Glenmore Hotel.',
            'The hotel on Big Moose Lake caters to wealthy vacationers, contrasting starkly with Mattie’s impoverished, ragged existence.',
            'Mattie befriends a sweet, fragile young hotel guest named Grace Brown, who arrived with her elegant beau, Chester Gillette.',
            'Grace is visibly anxious, weeping in dark hallways and clutching an intimate bundle of handwritten correspondence.',
            'On a sunny morning before embarking on a rowboat excursion with Chester, Grace approaches Mattie in great agitation.',
            'Grace presses the packet of letters into Mattie’s apron, begging her with tearful urgency: \'Burn them, Mattie. Promise you’ll burn them!\'',
            'Uncertain of their contents, Mattie tucks the mysterious bundle into her pocket, watching the couple row across the sparkling lake.'
        ]),
        ('Tragedy on Big Moose Lake', [
            'Hours later, search parties discover an empty, overturned rowboat floating near Punkey Bay on the desolate lake.',
            'The drowned body of Grace Brown is pulled from the frigid water; Chester Gillette is nowhere to be found, having fled the scene.',
            'Initial reports assume a tragic boating accident, but local authorities and doctors observe brutal blunt-force trauma on Grace’s head.',
            'Chester is apprehended days later in a nearby resort town, wearing dry clothes and falsely claiming Grace took her own life.',
            'Shock and horror sweep the Adirondacks as state prosecutors open an aggressive capital murder investigation.',
            'Retreating to her bed, Mattie hesitates to burn the letters, unlocking the twine to read Grace’s private, desperate words.',
            'The letters reveal that Grace was pregnant with Chester’s child, pleading with him to marry her to avoid public disgrace.'
        ]),
        ('Reading Grace’s Soul', [
            'Through Grace’s tender, agonizing letters, Mattie hears the authentic, desperate voice of a powerless young woman trapped by society.',
            'Chester had systematically deceived Grace, luring her to the remote lake with false marriage promises to silence her forever.',
            'Mattie realizes that burning the letters would destroy the sole conclusive evidence proving Chester’s premeditated murder.',
            'Simultaneously, Mattie confronts parallel traps in her own life as handsome young farmer Royal Loomis presses for marriage.',
            'Royal offers land, social respectability, and farm stability, but openly admits he will never allow books in his house.',
            'Her friend Minnie gives birth to twins in agony, trapped in a loveless marriage and warning Mattie not to surrender her mind.',
            'Mattie realizes that marrying Royal would extinguish her intellectual soul just as surely as the lake swallowed Grace.'
        ]),
        ('Racial Injustice & Moral Reckoning', [
            'Her brilliant black classmate Weaver Smith suffers a brutal assault by racist locals, and his hard-earned college savings are stolen.',
            'Despite the violence, Weaver refuses to abandon his dream, demonstrating heroic courage that deeply shames Mattie’s hesitation.',
            'Miss Wilcox is driven out of town when it is discovered that her estranged husband has suppressed her published poetry.',
            'Before leaving, Miss Wilcox leaves Mattie train fare to New York, urging her never to compromise her God-given voice.',
            'Mattie makes her fateful decision: she turns Grace Brown’s letters over to the district attorney, providing the decisive proof to convict Chester.',
            'By testifying and surrendering the letters, Mattie gives voice to the murdered Grace, ensuring justice for a forgotten woman.',
            'She breaks her engagement to Royal Loomis, returning his ring and enduring her father’s furious indignation.',
            'Mattie packs her modest cardboard suitcase, preparing to board the midnight train toward an uncertain future.'
        ]),
        ('Boarding the Train to New York', [
            'Under a magnificent starry Adirondack night, Mattie walks along the railway tracks toward the small whistle-stop station.',
            'Her younger sisters embrace her with tears of pride, urging their brilliant older sister to go and conquer the world.',
            'Weaver joins her on the platform, both brave young souls heading south toward university and intellectual emancipation.',
            'As the steam locomotive rolls into the station, Mattie looks out across the dark pine forests and mist-shrouded lakes of her youth.',
            'She carries Grace Brown’s memory in her heart, vowing to write stories that give dignity and truth to the silenced and the brave.',
            'The train whistle echoes across the ancient mountains as the wheels begin to turn, carrying Mattie into the gathering light.',
            'The novel concludes on an unforgettable, radiant anthem of female agency, artistic destiny, and triumphant moral courage.',
            'Mattie smiles through her tears, stepping boldly into the vast canvas of her own extraordinary life.'
        ]),
        [
            ('The Power of Voice & Storytelling', 'Celebrates the written word as an instrument of liberation, truth, and resurrection for silenced women.'),
            ('Autonomy vs. Female Subjugation', 'Deconstructs the historical socioeconomic cages—marriage, poverty, domestic servitude—that confined early 20th-century women.'),
            ('Historical Authenticity', 'Brilliantly weaves the real-life 1906 Grace Brown murder trial into a transcendent coming-of-age literary masterwork.'),
            ('Carnegie Medal Winner', 'Awarded the UK Carnegie Medal and Michael L. Printz Honor; hailed as an immortal classic of American historical fiction.')
        ]
    )

    # 16. Harry Potter and the Chamber of Secrets
    create_summary(
        'harry-potter-and-the-chamber-of-secrets', 'Harry Potter and the Chamber of Secrets', 'J.K. Rowling', 'Fantasy / Mystery / Adventure', '1998',
        'Little Whinging, The Burrow, Diagon Alley, Hogwarts School of Witchcraft and Wizardry, Scotland',
        [
            ('Harry Potter', 'A courageous twelve-year-old wizard who discovers he can speak Parseltongue and must confront Hogwarts’ darkest secret.'),
            ('Ron Weasley', 'Harry’s loyal, ginger-haired best friend whose family’s enchanted Ford Anglia aids their perilous adventures.'),
            ('Hermione Granger', 'The brilliant Muggle-born witch whose intellect deciphers the monster lurking within the castle plumbing.'),
            ('Tom Marvolo Riddle', 'The sinister sixteen-year-old memory of Lord Voldemort preserved inside an enchanted magical diary.'),
            ('Ginny Weasley', 'Ron’s shy first-year sister whose emotional vulnerability is manipulated by Riddle’s dark diary.'),
            ('Gilderoy Lockhart', 'The vain, incompetent Defense Against the Dark Arts professor whose heroic tales are fraudulent memory charms.'),
            ('Dobby', 'A devoted house-elf who uses extreme, chaotic methods to protect Harry from mortal danger at Hogwarts.'),
            ('Lucius Malfoy', 'A wealthy, haughty Death Eater who slips Voldemort’s dark relic into Ginny’s cauldron to ruin the Weasleys.')
        ],
        ('Warnings at Privet Drive', [
            'Trapped for the summer at the Dursleys’, twelve-year-old Harry Potter is visited by Dobby, an eccentric house-elf.',
            'Dobby warns Harry that mortal peril awaits him at Hogwarts, begging him not to return for his second year.',
            'When Harry refuses, Dobby shatters a pudding during an important dinner party, causing Uncle Vernon to lock Harry in his room.',
            'Ron Weasley and his twin brothers Fred and George rescue Harry in their father’s flying turquoise Ford Anglia.',
            'Harry spends an idyllic month at the warm, chaotic Weasley household, The Burrow, before traveling to Diagon Alley.',
            'At Flourish and Blotts, an altercation erupts between Arthur Weasley and Lucius Malfoy, who secretly plants a black diary with Ginny.'
        ]),
        ('The Message in Blood & The Petrifactions', [
            'Barred from Platform 9¾ by a sealed barrier, Harry and Ron fly the Ford Anglia to Hogwarts, crashing into the Whomping Willow.',
            'Harry begins hearing a sinister, disembodied chilling voice whispering murder from inside the castle’s stone walls.',
            'On Halloween night, caretaker Filch’s cat Mrs. Norris is found petrified, hanging near a message scrawled in gleaming blood:',
            '\'The Chamber of Secrets has been opened. Enemies of the heir, beware.\' Professor McGonagall explains the dark legend.',
            'Centuries earlier, founder Salazar Slytherin built a concealed chamber containing a monster to purge the school of Muggle-borns.',
            'During a dueling club demonstration, Harry unwittingly speaks Parseltongue to calm a serpent, terrifying the school.',
            'Classmates Colin Creevey and Justin Finch-Fletchley are petrified, turning the entire school against Harry as the suspected heir.'
        ]),
        ('Polyjuice Infiltration & Riddle’s Diary', [
            'Determined to prove whether Draco Malfoy is the Heir of Slytherin, Hermione brews illicit Polyjuice Potion in a girls’ bathroom.',
            'Harry and Ron disguise themselves as Crabbe and Goyle, interrogating Malfoy and discovering he knows nothing about the heir.',
            'Hermione is petrified by the creature, but Harry discovers a waterlogged, blank diary dropped in Moaning Myrtle’s flooded bathroom.',
            'Harry writes in the diary; ink sinks into the pages, and sixteen-year-old Tom Riddle responds, drawing Harry into his memory.',
            'Riddle shows Harry a memory from fifty years earlier, revealing that gamekeeper Rubeus Hagrid was expelled for harboring a monster.',
            'Ministry Minister Fudge and Lucius Malfoy suspend Headmaster Dumbledore and arrest Hagrid, sending him to Azkaban prison.',
            'Before leaving, Hagrid whispers cryptic instructions to Harry and Ron: \'Follow the spiders\'.'
        ]),
        ('The Forbidden Forest & Hermione’s Clue', [
            'Harry and Ron follow trails of fleeing spiders deep into the perilous depths of the Forbidden Forest at night.',
            'They are captured by Aragog, a monstrous blind acromantula spider raised by Hagrid in the castle five decades earlier.',
            'Aragog reveals that the monster from the Chamber was not a spider, but an ancient creature that spiders fear above all else.',
            'The giant spider colony prepares to devour the boys, but the feral flying Ford Anglia charges through the trees to rescue them.',
            'Returning to the hospital wing, Harry discovers a crumpled page from a library book clutched in petrified Hermione’s stiff hand.',
            'Hermione’s notes identify the beast: a Basilisk, a giant serpent whose direct gaze kills and whose reflected gaze petrifies.',
            'She deduced that the giant serpent moves unseen throughout Hogwarts by slithering through the ancient plumbing pipes.'
        ]),
        ('Descent into the Chamber & The Basilisk Slain', [
            'A new message appears: \'Her skeleton will lie in the chamber forever.\' Ginny Weasley has been abducted into the depths.',
            'Harry and Ron corner cowardly fraud Gilderoy Lockhart, forcing him at wandpoint to unlock the entrance beneath Myrtle’s sink.',
            'Sliding down slimy subterranean pipes, Lockhart attempts a memory charm with Ron’s broken wand; it backfires, causing a cave-in.',
            'Separated from Ron, Harry enters the Chamber alone, finding Ginny dying as Tom Riddle’s memory solidifies into physical form.',
            'Riddle anagrams his name into \'I am Lord Voldemort\', summoning the colossal Basilisk serpent to crush Harry in its coils.',
            'Fawkes the phoenix blinds the serpent and drops the Sorting Hat, from which Harry draws Godric Gryffindor’s ruby-hilted sword.',
            'Harry drives the blade into the Basilisk’s brain, slaying it, but is pierced by a venomous fang before Fawkes’s tears heal him.',
            'Harry drives the broken fang into Riddle’s diary; ink and black blood erupt as Riddle shrieks and dissolves into oblivion.'
        ]),
        ('The Freedom of Dobby & Rebirth', [
            'Ginny awakens fully restored, weeping in relief as Harry escorts her and Ron back to Professor McGonagall’s office.',
            'Dumbledore returns to the castle, reassuring Ginny that Voldemort exploited her innocence through a dark enchanted relic.',
            'Lucius Malfoy storms in with his abused house-elf Dobby, enraged that his conspiracy to unseat Dumbledore has failed.',
            'Harry deduces that Malfoy slipped the diary to Ginny, tricking Lucius into freeing Dobby by concealing the ruined book in his sock.',
            'When Lucius hurls the sock aside, Dobby catches it, gaining his freedom and blasting his furious former master backward.',
            'The petrified victims, including Hermione and Colin Creevey, are revived by Mandrake restorative draught at an ecstatic feast.',
            'Gryffindor wins the House Cup, examinations are canceled, and Hagrid returns triumphantly from Azkaban to thunderous applause.',
            'The novel closes on Harry boarding the Hogwarts Express with joy, anchored by true friendship and courageous moral choices.'
        ]),
        [
            ('The Nature of Choice vs. Blood', 'Dumbledore delivers the foundational series maxim: \'It is our choices that show what we truly are, far more than our abilities.\''),
            ('Prejudice & Social Hierarchy', 'Critiques pure-blood supremacist ideology and the exploitation of enslaved beings through the plight of Dobby.'),
            ('The Power of Memory & Manipulation', 'Explores the psychological danger of trusting unverified magical objects through Tom Riddle’s seductive enchanted diary.'),
            ('Classic Mystery Structure', 'Combines schoolboy gothic humor with an intricately plotted, clue-driven detective narrative that delighted millions globally.')
        ]
    )

    # 17. Harry Potter and the Prisoner of Azkaban
    create_summary(
        'harry-potter-and-the-prisoner-of-azkaban', 'Harry Potter and the Prisoner of Azkaban', 'J.K. Rowling', 'Fantasy / Mystery / Adventure', '1999',
        'Little Whinging, The Knight Bus, The Leaky Cauldron, Hogwarts, Hogsmeade, The Shrieking Shack, Scotland',
        [
            ('Harry Potter', 'A thirteen-year-old wizard targeted by a purported mass murderer while learning to master the Patronus Charm.'),
            ('Sirius Black', 'The notorious escaped prisoner of Azkaban, believed to be Voldemort’s right hand, but actually Harry’s innocent godfather.'),
            ('Remus Lupin', 'The compassionate, impoverished Defense Against the Dark Arts teacher who conceals his tragic identity as a werewolf.'),
            ('Peter Pettigrew', 'The cowardly animagus traitor masquerading for twelve years as Ron’s pet rat Scabbers.'),
            ('Hermione Granger', 'Harry’s brilliant friend whose secret Time-Turner and analytical mind prove vital to altering destiny.'),
            ('Ron Weasley', 'Harry’s fiercely loyal comrade who defends his mangy pet rat until its horrifying true identity is unmasked.'),
            ('Severus Snape', 'The bitter Potions master whose childhood grudge against James Potter and Sirius Black blinds him to truth.'),
            ('Buckbeak', 'A proud, majestic Hippogriff sentenced to death by the Ministry after being provoked by Draco Malfoy.')
        ],
        ('Aunt Marge & The Knight Bus Escape', [
            'During summer at Privet Drive, thirteen-year-old Harry Potter is pushed beyond endurance by Aunt Marge’s vicious insults.',
            'Losing control of his magic, Harry accidentally inflates Marge like a balloon and flees into the midnight streets with his trunk.',
            'In the dark suburban shadows, Harry spots the terrifying silhouette of an enormous black dog watching him from the bushes.',
            'He is rescued by the Knight Bus, a purple triple-decker vehicle carrying stranded wizards at breakneck speeds across Britain.',
            'Minister Fudge greets Harry at the Leaky Cauldron, surprisingly dismissing his magical violation without disciplinary action.',
            'Harry discovers why: mass murderer Sirius Black has broken out of Azkaban, purportedly hunting Harry to avenge Lord Voldemort.'
        ]),
        ('Dementors, Boggarts & The Marauder’s Map', [
            'Aboard the Hogwarts Express, hooded rotting Dementors board the train; Harry faints in terror as chilling despair engulfs him.',
            'New Defense teacher Professor Remus Lupin revives Harry with chocolate, having driven the foul creature away with magic.',
            'At Hogwarts, Lupin teaches practical defense, guiding students to conquer fear Boggarts with laughter and *Riddikulus*.',
            'Fred and George Weasley gift Harry the Marauder’s Map, showing every secret passage and real-time footprint inside Hogwarts.',
            'Sneaking into wizard village Hogsmeade beneath his Invisibility Cloak, Harry overhears teachers discussing Sirius Black.',
            'Black was James Potter’s best friend, best man, and Harry’s godfather, who allegedly betrayed the Potters and murdered Pettigrew.',
            'Shattered by the revelation of Black’s supposed treachery, Harry burns with fury and vows to confront his parents’ betrayer.'
        ]),
        ('The Patronus Charm & Buckbeak’s Trial', [
            'Lupin gives Harry private lessons against Dementors, teaching him to project a silver shield with the incantation *Expecto Patronum*.',
            'Drawing upon intense happy memories, Harry slowly masters the difficult charm, determined to resist the soul-sucking wraiths.',
            'Hagrid’s proud Hippogriff Buckbeak is sentenced to decapitation after being provoked and scratched by a spiteful Draco Malfoy.',
            'Hermione suffers exhaustion from an impossible class schedule, mysteriously appearing in multiple overlapping classrooms at once.',
            'Ron’s pet rat Scabbers vanishes, leaving blood on the bedsheets; Ron bitterly blames Hermione’s half-Kneazle cat Crookshanks.',
            'On execution day, the trio visits Hagrid’s cabin to comfort him before hearing the executioner’s axe fall in the pumpkin patch.',
            'As they retreat in tears, Scabbers bites Ron’s finger, and a monstrous black dog erupts from the trees, dragging Ron into the earth.'
        ]),
        ('The Shrieking Shack & Traitor Unmasked', [
            'Harry and Hermione plunge into a secret tunnel beneath the Whomping Willow, entering the notorious haunted Shrieking Shack.',
            'The black dog transforms into the wild-eyed Sirius Black; Harry tackles him, preparing to kill his parents’ betrayer.',
            'Professor Lupin bursts into the room, disarming Harry and astonishing the teenagers by embracing Sirius as a beloved brother.',
            'Hermione deduces that Lupin is a werewolf; Severus Snape arrives under an Invisibility Cloak, eager to feed Sirius to Dementors.',
            'The three students simultaneously disarm Snape, knocking him unconscious against the wall to demand the complete truth.',
            'Sirius and Lupin reveal that Peter Pettigrew was the secret Death Eater who sold the Potters, framed Black, and faked his death.',
            'They force rat Scabbers into the room, casting an animagus reversal spell that reveals the sniveling, treacherous Peter Pettigrew.'
        ]),
        ('Werewolf Chaos, Dementor Swarm & Time-Turner', [
            'Harry spares Pettigrew’s life, refusing to let Sirius become a killer and intending to deliver Pettigrew to Azkaban to clear Sirius.',
            'Sirius offers Harry a real home with his godfather once exonerated, filling Harry with profound joy and anticipation.',
            'As they emerge beneath the night sky, the full moon rises; Lupin, having forgotten his wolfsbane potion, transforms into a feral werewolf.',
            'Sirius shifts into a great dog to defend them, while Pettigrew seizes a wand, turns back into a rat, and vanishes into the darkness.',
            'Dozens of Dementors sweep across the lake to consume Sirius and Harry; a radiant silver stag gallops across the water, saving them.',
            'Awakening in the hospital wing with Sirius captured in a locked tower, Dumbledore advises Hermione to use her secret Time-Turner.',
            'Hermione loops the golden chain around Harry, spinning the hourglass back three hours to relive the harrowing evening from the shadows.',
            'They sneak into the pumpkin patch and rescue Buckbeak the Hippogriff moments before the executioner’s heavy axe can fall.'
        ]),
        ('Flight on Hippogriff Wings & Sirius Freed', [
            'Waiting across the dark lake, Harry realizes the wizard who cast the silver stag was not his father’s ghost, but his future self.',
            'Harry steps onto the shore, raises his wand with triumphant conviction, and unleashes an immortal, blinding silver stag Patronus.',
            'The stag drives back the hundreds of Dementors, rescuing past Harry and Sirius from having their souls consumed.',
            'Riding Buckbeak through the night sky, Harry and Hermione land at the tower window, blasting the iron bars to liberate Sirius.',
            'Sirius embraces his godson in overflowing gratitude before flying into the starry heavens astride the magnificent Hippogriff.',
            'Snape rages uncontrollably at Sirius’s escape, while Lupin resigns with dignity after his werewolf condition is leaked.',
            'Aboard the train home, a tiny owl arrives carrying a letter from Sirius granting Harry permission to visit Hogsmeade in third year.',
            'The novel closes on Harry Potter returning to the Muggle world with joy, dignity, and the enduring love of his living godfather.'
        ]),
        [
            ('The Subjectivity of Fear & Mastery', 'Positions the Dementors as profound psychological metaphors for depression, conquered only through deliberate hope.'),
            ('The Power of Choice over Prophecy', 'Explores how mercy (sparing Pettigrew) and agency (casting the Patronus) shape moral destiny over predetermined fate.'),
            ('The Flaws of Authority & Justice', 'Critiques the Ministry of Magic’s punitive cruelty and bureaucratic blindness in employing soul-destroying Dementors.'),
            ('Series Turning Point', 'Widely hailed by critics and scholars as the finest narrative achievement of J.K. Rowling’s Harry Potter canon.')
        ]
    )

if __name__ == '__main__':
    run()
