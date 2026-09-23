#!/usr/bin/env python3
"""
novels_part1.py — Generates summaries for novels 1 to 9.
"""

from build_all_summaries import create_summary

def run():
    # 1. The King of Torts
    create_summary(
        'the-king-of-torts', 'The King of Torts', 'John Grisham', 'Legal Thriller', '2003',
        'Washington D.C., federal courtrooms, corporate pharmaceutical headquarters',
        [
            ('Clay Carter', 'An underpaid Washington D.C. public defender catapulted to immense wealth and toxic notoriety.'),
            ('Max Pace', 'A shadowy corporate fixer orchestrating clandestine pharmaceutical payouts and mass tort schemes.'),
            ('Patton French', 'A flamboyant, ultra-wealthy Florida trial attorney who pilots private jets and finances mega-lawsuits.'),
            ('Rebecca Van Horn', 'Clay’s high-society fiancée whose wealthy father disdains Clay’s public defender career.'),
            ('Ridley', 'Clay’s loyal, overworked associate who follows him from the public defenders office into corporate chaos.'),
            ('Tequila Watson', 'A young addict whose inexplicable murder confession uncovers a deadly clinical drug coverup.'),
            ('Jocelyn Baker', 'Clay’s sharp legal assistant who helps coordinate the tidal wave of incoming class-action claimants.'),
            ('Ken Burnside', 'Opposing corporate counsel defending multibillion-dollar pharmaceutical conglomerates.')
        ],
        ('Public Defender in Crisis', [
            'Clay Carter spends five grueling years at the Washington Public Defender’s Office earning a meager wage.',
            'He is assigned the routine murder defense of Tequila Watson, a young man who inexplicably shot a stranger on the street.',
            'Watson exhibits strange psychotic dissociation, swearing he had never met the victim and possessed no motive for the shooting.',
            'Investigating Watson’s background, Clay discovers a startling parallel murder committed by another young addict named Pumpkin Pumphrey.',
            'Clay tracks medical records and realizes both killers were recently enrolled in clinical treatment programs for drug rehabilitation.',
            'Frustrated by low pay and pressured by his fiancée’s wealthy father, Clay desperately searches for an escape from his stagnant career.'
        ]),
        ('The Maxipril Conspiracy', [
            'Clay is secretly contacted by Max Pace, a mysterious operative representing a major pharmaceutical conglomerate.',
            'Pace reveals that both killers took Maxipril, an unapproved acne drug causing violent, homicidal psychotic breaks in a small percentage of patients.',
            'To prevent an open public scandal, Pace offers Clay a covert fund of fifteen million dollars to settle claims quietly with victims’ families.',
            'Clay faces a profound ethical dilemma: expose the killer drug publicly or accept immense wealth under confidentiality agreements.',
            'Seduced by wealth and prestige, Clay resigns from the public defender’s office and incorporates his own boutique firm, Carter & Associates.',
            'He orchestrates swift, silent settlements for Maxipril victims, taking enormous contingency cuts that instantly make him a multimillionaire.',
            'News leaks of Clay’s sudden overnight fortune, instantly attracting the attention of rival class-action litigators across the country.'
        ]),
        ('Crowning the King of Torts', [
            'Max Pace returns with a far more lucrative target: Dypar, a popular chemotherapy drug manufactured by Ackerman Labs causing terminal tumors.',
            'Pace instructs Clay to launch a massive nationwide tort lawsuit against Ackerman, leveraging confidential inside dossiers.',
            'Clay launches aggressive television advertising campaigns, recruiting thousands of dying patients to join his massive class-action suit.',
            'Ackerman Labs capitulates under negative media frenzy, settling the Dypar mass tort for hundreds of millions of dollars.',
            'Clay takes a staggering legal fee, buys a multimillion-dollar Georgetown mansion, and acquires a private Gulfstream jet.',
            'The national press dubs Clay the new \'King of Torts\', celebrating his meteoric rise from obscure defender to legal royalty.',
            'Drunk on power, Clay alienates his loyal colleagues and severs ties with Rebecca as his lifestyle grows increasingly decadent.'
        ]),
        ('The Tarvan Trap & Mass Hysteria', [
            'Hungry for an unprecedented multibillion-dollar victory, Clay sets his sights on Tarvan, a blockbuster anti-cholesterol medication.',
            'Manufactured by Goffman Labs, Tarvan is consumed by millions of Americans, representing a potential trillion-dollar jackpot.',
            'Clay borrows tens of millions of dollars from predatory hedge funds and trial lawyer kingpin Patton French to fund litigation.',
            'He signs up tens of thousands of dubious claimants through relentless nationwide advertising blitzes and toll-free hotlines.',
            'Goffman Labs refuses to settle, adamantly maintaining that Tarvan is completely safe and rigorously tested.',
            'Clay’s firm is stretched to its financial breaking point under astronomical interest payments, payroll expenses, and luxury overhead.',
            'Max Pace suddenly vanishes without a trace, leaving Clay entirely exposed to aggressive corporate defense litigators.'
        ]),
        ('The Courtroom Collapse', [
            'The first Tarvan bellwether trial begins in federal court; independent medical experts testify that Tarvan caused zero adverse effects.',
            'The jury returns a swift, devastating defense verdict, completely exonerating Goffman Labs and finding no medical liability.',
            'Wall Street reacts instantly; Tarvan stock rebounds, while Clay’s class-action empire implodes under crushing debt.',
            'Clay is blindsided by investigative revelations that Max Pace was an arbitrageur manipulating stock swings through Clay’s lawsuits.',
            'The Securities and Exchange Commission and federal grand juries launch criminal insider trading probes into Clay’s operations.',
            'Patton French and angry lenders demand immediate repayment of loans, foreclosing on Clay’s assets, townhouses, and aircraft.',
            'Enraged former clients, whose legitimate claims were botched by Clay’s rushed settlements, file massive malpractice suits.',
            'Clay is physically assaulted on the street by a furious former client, sustaining severe injuries that leave him hospitalized.'
        ]),
        ('Disbarment, Ruin & Redemption', [
            'Stripped of his legal license and declared completely bankrupt, Clay watches his legal empire collapse into dust.',
            'He surrenders his vehicles, private jet, and Georgetown estate to bankruptcy liquidators and federal tax authorities.',
            'Rebecca Van Horn marries another wealthy suitor, leaving Clay to confront the utter emptiness of his greed-driven ambitions.',
            'Federal prosecutors agree not to pursue felony prison sentences in exchange for Clay’s complete testimony against corporate manipulators.',
            'Humbled and penniless, Clay realizes his happiest, most honorable days were spent defending indigent clients at the public defenders desk.',
            'Accompanied by Ridley, his steadfast former associate, Clay quietly leaves the United States for an unpretentious new life in London.',
            'He vows never to practice mass litigation again, having experienced the seductive corruption and catastrophic fall of the tort industry.',
            'Clay finds peace in anonymity, trading the hollow crown of legal royalty for moral clarity and personal redemption.'
        ]),
        [
            ('The Corruption of Legal Ethics', 'Exposes how contingency-fee mass torts can transform civil justice into predatory financial speculation.'),
            ('The Illusion of Fast Wealth', 'Illustrates how unchecked ambition and greed erode professional integrity and personal relationships.'),
            ('Corporate Manipulation', 'Reveals the dark nexus between pharmaceutical giants, hedge fund arbitrageurs, and legal mercenaries.'),
            ('Literary Impact', 'Grisham delivers a gripping, cautionary legal thriller dissecting the systemic excesses of the American tort system.')
        ]
    )

    # 2. A Week in Winter
    create_summary(
        'a-week-in-winter', 'A Week in Winter', 'Marcia Willett', 'Contemporary Fiction', '2001',
        'Moorgate farmhouse on the edge of Exmoor, Devon, South West England',
        [
            ('Maudie Todhunter', 'An elderly, graceful widow contemplating the painful sale of her beloved ancestral farmhouse.'),
            ('Frances Todhunter', 'Maudie’s ambitious, calculating daughter-in-law determined to liquidate Moorgate for her own social advancement.'),
            ('Rob Todhunter', 'Maudie’s well-meaning stepson, torn between filial loyalty to Maudie and the mounting financial demands of his wife.'),
            ('Selina', 'Rob’s perceptive, caring sister who provides emotional sanctuary and moral balance to the fragmented family.'),
            ('Cleo', 'Selina’s goddaughter, nursing acute heartbreak after an affair with a selfish, married older man.'),
            ('Hugh', 'Frances’s gentle, disenchanted brother, recovering from a bruising divorce and seeking peace in the countryside.'),
            ('Ned', 'A loyal, longstanding rural neighbor deeply connected to the traditions and rhythms of the Devon landscape.'),
            ('Posy', 'Maudie’s devoted companion animal whose quiet presence anchors the warmth of the farmhouse kitchen.')
        ],
        ('The Impending Loss of Moorgate', [
            'Maudie Todhunter faces an agonizing winter milestone following the passing of her husband at their historic home, Moorgate.',
            'Perched upon the rugged, windswept border of Exmoor, the old stone farmhouse holds decades of cherished memories and quiet sorrows.',
            'With heating costs soaring and maintenance overwhelming her failing health, Maudie reluctantly agrees to put the estate on the market.',
            'Her daughter-in-law Frances views Moorgate merely as a lucrative asset to fund an opulent lifestyle and prestige school fees.',
            'Frances aggressively pressures Maudie and Rob to accept the highest commercial developer bid without regard for the land’s heritage.',
            'Maudie resolves to spend one final, reflective winter week at Moorgate surrounded by those she loves before surrendering the keys.'
        ]),
        ('Arrival of Wounded Wanderers', [
            'Seeking refuge from emotional devastation in London, young Cleo accepts an invitation from her godmother Selina to join Maudie.',
            'Cleo is reeling from the agonizing discovery that her charismatic older lover was callously stringing her along without intent to leave his wife.',
            'Arriving amidst a sudden, biting winter gale, Cleo is greeted by roaring hearth fires, hot tea, and Maudie’s unhurried kindness.',
            'Frances’s brother Hugh unexpectedly arrives at Moorgate seeking escape from the bitter fallout of his own finalized divorce.',
            'Exhausted by city pretense and corporate rat-races, Hugh finds an immediate kinship with the serene isolation of the moorland farmhouse.',
            'The disparate group forms an impromptu sanctuary against the freezing wind howling across the Exmoor hills.',
            'Beneath the quiet domestic routines of cooking and walking, each visitor carries unhealed wounds requiring solace.'
        ]),
        ('The Snowstorm & Fireside Confessions', [
            'A heavy Devon blizzard blankets the roads in impassable snowdrifts, cutting Moorgate completely off from the modern world.',
            'Trapped by the severe weather, the residents gather nightly around the wood-burning stove, sharing long-buried truths.',
            'Maudie reveals the bittersweet history of her youth, confessing that her marriage was respectful rather than passionately romantic.',
            'She shares memories of her true lost love, a wartime pilot whose memory she preserved without bitterness or public regret.',
            'Listening to Maudie’s quiet resilience, Cleo begins to view her own romantic disillusionment through a broader, mature lens.',
            'Hugh watches Cleo’s delicate vulnerability transform into courage, discovering feelings of admiration that stir his guarded heart.',
            'The shared isolation acts as an emotional crucible, stripping away social defenses and fostering profound bonds.'
        ]),
        ('Frances Strikes & Domestic Intrigue', [
            'Oblivious to the deep human healing unfolding at Moorgate, Frances telephones persistently with aggressive real-estate demands.',
            'She disparages Maudie’s sentimentality, demanding that Rob push through a hasty sale before property market values fluctuate.',
            'Rob visits the farmhouse and is deeply moved by the peace radiating from Maudie, Cleo, and his brother-in-law Hugh.',
            'For the first time, Rob confronts Frances’s relentless materialism, questioning whether his marriage can survive her self-absorbed vanity.',
            'Hugh openly challenges his sister’s coldness, defending Maudie’s right to determine the ultimate destiny of her home.',
            'A long-lost family document surfaces in the attic desk, revealing historical covenants governing Moorgate’s ancestral boundaries.',
            'The revelation throws Frances’s developer negotiations into legal jeopardy, shifting the balance of power back to Maudie.'
        ]),
        ('Crucibles of the Moorland', [
            'A sudden winter crisis occurs when Cleo wanders onto the high moor during a fleeting break in the storm and is overtaken by mist.',
            'Hugh and neighbor Ned launch an urgent search across the treacherous peat bogs, guided by local knowledge and instinct.',
            'Hugh discovers Cleo shivering near an ancient granite stone, wrapping her in his coat and carrying her safely back to the hearth.',
            'The brush with danger cements an unspoken romantic devotion between Hugh and Cleo, forged in shared vulnerability.',
            'Maudie witnesses their blossoming tenderness, recognizing that the farmhouse continues to generate new life and enduring hope.',
            'Frances arrives unexpectedly as the snow plows clear the road, demanding an immediate contract signing from the family.',
            'Confronted by the unified moral solidarity of Maudie, Rob, Hugh, and Selina, Frances realizes her manipulative control is broken.',
            'Rob finally asserts his independence, refusing to coerce Maudie and insisting on honoring his stepmother’s wishes.'
        ]),
        ('A Legacy Preserved & New Beginnings', [
            'Maudie announces her definitive decision: Moorgate will not be sold to commercial developers for demolition or subdivision.',
            'Instead, she arranges for the property to be leased and preserved, allowing Hugh and Cleo to establish a rural retreat.',
            'Cleo decides to leave London permanently, embracing countryside literature and finding true partnership with Hugh.',
            'Frances departs in bitter indignation, while Rob experiences profound liberation and reconciles his relationship with Maudie.',
            'The winter week concludes with clear skies, melting snow, and golden sunlight breaking over the Exmoor hills.',
            'Maudie prepares to move into a manageable seaside cottage in nearby Dartmouth, content that Moorgate’s spirit remains intact.',
            'The ancient farmhouse stands proud against the elements, a testament to endurance, hospitality, and unconditional love.',
            'Each visitor departs fundamentally transformed, carrying renewed purpose and healed hearts into the approaching spring.'
        ]),
        [
            ('Healing Power of Place', 'Explores how physical sanctuary and natural landscapes offer solace and restorative clarity to bruised spirits.'),
            ('Generational Reconciliation', 'Contrasts predatory materialism with ancestral stewardship, family loyalty, and emotional generosity.'),
            ('Resilience in Winter', 'Uses the harsh Devon climate as a resonant metaphor for emotional endurance, grief, and eventual springtime renewal.'),
            ('Literary Craft', 'Marcia Willett’s warm, observant character studies evoke Rosamunde Pilcher’s timeless traditions of English pastoral fiction.')
        ]
    )

    # 3. The Last Detective
    create_summary(
        'the-last-detective', 'The Last Detective', 'Robert Crais', 'Crime Fiction / Mystery', '2003',
        'Los Angeles, Hollywood Hills, Louisiana bayous, Vietnam flashback sequences',
        [
            ('Elvis Cole', 'A wisecracking Los Angeles private investigator haunted by unresolved combat trauma from his Vietnam tour.'),
            ('Joe Pike', 'Cole’s enigmatic, indomitable former Marine partner whose lethal combat discipline provides essential backup.'),
            ('Lucy Chenier', 'Elvis’s loving partner, a Louisiana attorney whose life is shattered when her young son is snatched in California.'),
            ('Ben Chenier', 'Lucy’s bright ten-year-old son who adores Elvis but becomes a hostage in a sadistic vendetta.'),
            ('Richard Chenier', 'Ben’s wealthy, arrogant father who blames Cole for the abduction and hires ruthless private security mercenaries.'),
            ('Dodge / Tran', 'A brilliant, vengeful sniper whose childhood family was obliterated in a clandestine Vietnam operation involving Cole.'),
            ('Carol Starkey', 'A battle-scarred LAPD detective and Cole’s trusted ally navigating bureaucratic police department politics.'),
            ('John Meyer', 'A corrupt federal intelligence operative willing to sacrifice lives to conceal black-budget war crimes.')
        ],
        ('The Disappearance on the Deck', [
            'Private investigator Elvis Cole is enjoying a sunny afternoon at his Hollywood Hills home, babysitting young Ben Chenier.',
            'While Lucy is downtown finalizing legal meetings, Elvis steps inside for mere minutes to answer an urgent telephone call.',
            'When he returns to the sun deck overlooking the canyon, ten-year-old Ben has vanished without a single sound or struggle.',
            'A frantic search of the property and hillside brush reveals only a single cryptic calling card left upon the outdoor table.',
            'Elvis contacts the LAPD and his lethal, hyper-vigilant partner Joe Pike, initiating an immediate covert search grid.',
            'The phone rings; an icy, chilling voice informs Cole that this is not a ransom kidnapping, but an overdue execution of justice.'
        ]),
        ('A Ghost from the Mekong Delta', [
            'The kidnapper reveals intimate, classified details regarding Cole’s military service as an elite Army Ranger in Vietnam.',
            'Elvis is subjected to sadistic psychological taunts, accused of slaughtering an innocent Vietnamese family during a 1972 jungle raid.',
            'Lucy arrives at the residence, utterly devastated by the disappearance and terrified by the grotesque threats against her son.',
            'Richard Chenier flies in from Louisiana on a private jet, bitterly berating Elvis and deploying private security mercenaries to find Ben.',
            'Lucy’s trust in Elvis shatters under the weight of panic, accusing him of bringing deadly violence into her child’s world.',
            'Recognizing that law enforcement and private security are outmatched, Elvis and Pike operate beneath the official radar.',
            'Elvis must confront repressed memories of the brutal secret war he fought decades ago in the jungles of Southeast Asia.'
        ]),
        ('Unraveling the Blood Debt', [
            'Joe Pike leverages his shadowy military contacts to trace the encrypted communication channels used by the kidnapper.',
            'LAPD detective Carol Starkey provides critical forensic data, discovering military-grade surveillance bugs around Cole’s home.',
            'The investigation reveals the kidnapper’s identity: a lethal operative known as Dodge, born Tran Van Noc in a Mekong delta hamlet.',
            'During a classified Phoenix-style intelligence mission, Cole’s unit was ordered into Tran’s village to eliminate enemy infiltrators.',
            'A catastrophic friendly-fire airstrike called in by corrupt CIA handlers incinerated Tran’s parents and siblings before his eyes.',
            'Cole had pulled the surviving young boy from the burning wreckage, but Tran grew up nursing a consuming desire for vengeance.',
            'Tran spent thirty years mastering military assassination, tracking Cole across continents to extract the ultimate retaliatory agony.'
        ]),
        ('The Mercenary Crossfire', [
            'Richard Chenier’s private security mercenaries attempt an unauthorized ambush based on a false electronic trace in downtown LA.',
            'Dodge anticipates the assault with terrifying tactical superiority, detonating claymore mines and slaughtering the mercenaries.',
            'Dodge transmits horrifying proof-of-life footage showing Ben locked inside an airtight containment crate in an undisclosed location.',
            'He issues an ultimatum: Cole must present himself alone at a specified location without police backup, or Ben suffocates.',
            'Lucy breaks down completely, pleading with Elvis to surrender his life to save her only child from the madman’s grip.',
            'Joe Pike refuses to let Cole walk into a suicide trap alone, crafting a high-risk counter-assault strategy.',
            'Elvis realizes that Dodge does not merely want his corpse; he wants Cole to endure total moral and psychological annihilation.'
        ]),
        ('Climax at the Industrial Plant', [
            'Cole travels to an abandoned industrial manufacturing complex located in the desolate badlands of outer Los Angeles county.',
            'Dodge ambushes Cole from hidden catwalks, subjecting him to a brutal physical beating while delivering a harrowing ideological sermon.',
            'He forces Cole to look into video monitors displaying Ben’s rapidly diminishing oxygen supply inside the sealed tank.',
            'Cole acknowledges the horrifying atrocities of the Vietnam War, but refuses to let an innocent ten-year-old pay for historical sins.',
            'Joe Pike breaches the facility perimeter, engaging Dodge’s perimeter snipers with surgical precision and lethal rifle fire.',
            'A fierce, visceral hand-to-hand fight erupts between Cole and Dodge amidst shattered machinery and high-voltage wiring.',
            'Cole overcomes Dodge’s blade attack, subduing the assassin and forcing the override codes to release the locked containment vessel.',
            'Ben is pulled from the tank unconscious but alive, rushed to paramedic trauma teams as emergency sirens flood the valley.'
        ]),
        ('Fractured Bonds & The Lonely Sentinel', [
            'Ben makes a full medical recovery in pediatric intensive care, embracing his tearful mother in an emotional reunion.',
            'Richard Chenier prepares to take Lucy and Ben back to Louisiana, determined to insulate his family from further West Coast peril.',
            'Despite his heroic rescue, the emotional rupture between Elvis and Lucy proves too deep and traumatic to repair.',
            'Lucy acknowledges Cole’s heroism, but confesses that she will never look at him without seeing the mortal danger that took her child.',
            'Elvis watches in silent heartache as Lucy and Ben depart for the airport, accepting the tragic isolation of his calling.',
            'Pike stands silently by his friend’s side on the canyon deck, affirming their unbreakable brotherhood forged in adversity.',
            'Cole is left to reconcile his lingering combat ghosts, recognizing that the scars of war never truly fade from memory.',
            'The novel closes on Elvis standing vigil over Los Angeles, an enduring, bruised protector dedicated to defending the innocent.'
        ]),
        [
            ('The Long Shadow of War', 'Examines how wartime guilt, moral injury, and collateral violence reverberate across decades and generations.'),
            ('The Price of Devotion', 'Explores the fragile, vulnerable boundary between protective paternal love and catastrophic personal risk.'),
            ('Brotherhood & Loyalty', 'Deepens the iconic partnership between Cole and Joe Pike, highlighting unspoken loyalty as an unbreakable anchor.'),
            ('Critical Acclaim', 'Hailed by critics as Robert Crais’s most emotionally complex, mature, and gripping private investigator masterpiece.')
        ]
    )

    # 4. Eat Cake
    create_summary(
        'eat-cake', 'Eat Cake', 'Jeanne Ray', 'Contemporary Domestic Fiction', '2003',
        'Suburban Chicago, Illinois, domestic kitchen and family home',
        [
            ('Ruth Steiner', 'A devoted suburban mother and wife who channels anxiety, love, and domestic stress into artisanal baking.'),
            ('Sam Steiner', 'Ruth’s hardworking husband whose sudden corporate executive layoff plunges the household into financial crisis.'),
            ('Camille Steiner', 'Ruth and Sam’s bright, ambitious high-school daughter preparing to enter an expensive elite university.'),
            ('Marion', 'Ruth’s eccentric, sharp-tongued mother who breaks both wrists and moves in, demanding relentless care.'),
            ('Guy', 'Ruth’s flamboyant, estranged father who arrives uninvited after losing his longtime partner and life savings.'),
            ('Mrs. Ferguson', 'A discerning neighborhood gourmet society matron whose glowing praise launches Ruth’s culinary reputation.'),
            ('Arthur', 'Sam’s loyal corporate colleague who provides moral support and helps navigate the harsh modern job market.'),
            ('Nora', 'Ruth’s encouraging neighbor who assists in coordinating ingredient deliveries and packing pastry boxes.')
        ],
        ('Domestic Equilibrium Shattered', [
            'Ruth Steiner has lived a comfortable, predictable life in suburban Chicago managing her household with gentle precision.',
            'Her supreme therapeutic outlet has always been the kitchen, where whipping meringues and measuring flour calms her restless nerves.',
            'Without warning, her husband Sam is fired from his high-level executive position during an aggressive corporate merger.',
            'Faced with a heavy mortgage, zero income, and daughter Camille’s upcoming college tuition, the family is plunged into panic.',
            'Sam slips into deep depression, spending days in his pajamas obsessively scanning executive classifieds without success.',
            'Ruth retreats to the kitchen, baking an elaborate seven-layer chocolate hazelnut torte to keep her spiraling fears at bay.'
        ]),
        ('The Influx of Dysfunctional Parents', [
            'Ruth’s fragile household equilibrium collapses further when her elderly mother Marion falls and fractures both wrists.',
            'Unable to feed, dress, or bathe herself, the imperious and hypercritical Marion moves into the Steiner guest bedroom.',
            'Marion demands constant attention, criticizing Ruth’s cooking, housekeeping, and parenting from dawn until dusk.',
            'Days later, Ruth’s estranged, theatrical father Guy arrives on the doorstep carrying antique luggage and weeping bitterly.',
            'Having lost his life partner and squandered his savings, Guy moves into the cramped basement rec room without hesitation.',
            'Ruth finds herself trapped under one roof with two divorced, narcissistic parents who have despised each other for thirty years.',
            'With her home transformed into a combat zone and bills mounting, Ruth begins baking around the clock to survive the madness.'
        ]),
        ('The Alchemy of Flour and Sugar', [
            'Ruth transforms her kitchen into a professional bakery laboratory, producing lemon chiffon, rum cakes, and almond tortes.',
            'The intoxicating aromas of melted dark chocolate, vanilla bean, and toasted pecans drift through the neighborhood streets.',
            'Marion and Guy continue their verbal skirmishes at breakfast, but find themselves temporarily silenced by Ruth’s warm pastries.',
            'Camille takes Ruth’s cakes to school events and charity bake sales, where attendees fight over the last remaining slices.',
            'Mrs. Ferguson, a wealthy local society matron, tastes a slice of Ruth’s orange-almond sponge and is instantly captivated.',
            'She offers Ruth hundreds of dollars to bake specialized desserts for an upcoming high-society gala dinner.',
            'Recognizing an unexpected lifeline, Ruth accepts the commission, working through the night to fulfill the order.'
        ]),
        ('A Family Mobilizes in the Kitchen', [
            'The society gala is an overwhelming triumph, prompting an avalanche of telephone orders from country clubs and restaurants.',
            'Ruth realizes she cannot manage the commercial baking volume alone without turning her house into an industrial facility.',
            'Seeing Ruth on the verge of exhaustion, her dysfunctional family unexpectedly sets aside their grievances to pitch in.',
            'Sam discovers a renewed sense of purpose by managing inventory, sourcing wholesale flour, and balancing the company books.',
            'Her flamboyant father Guy takes charge of cake decorating, applying his artistic flair to craft exquisite sugar flowers.',
            'Even sharp-tongued Marion contributes, using her healed fingers to fold pastry boxes and handle customer phone calls.',
            'Camille sets up a website and coordinates deliveries across the Chicago suburbs in the family station wagon.'
        ]),
        ('Crises of Capacity & Commercial Triumph', [
            'As wedding season approaches, Ruth is commissioned to create a massive five-tier wedding cake for a prominent socialite family.',
            'A catastrophic electrical blackout strikes the neighborhood during a summer storm, threatening to ruin dozens of refrigerated tiers.',
            'The entire family rallies heroically, loading cakes into coolers and securing emergency generator power from generous neighbors.',
            'Guy and Marion work side-by-side for the first time in decades, meticulously piping buttercream rosettes by candlelight.',
            'The magnificent wedding cake is delivered on time, drawing gasps of wonder from hundreds of reception guests.',
            'A prestigious culinary magazine features Ruth’s boutique baking enterprise on its cover, guaranteeing long-term commercial success.',
            'Sam receives several executive job offers, but realizes he prefers running the thriving family business alongside his wife.',
            'Local culinary critics celebrate Ruth’s artistry, declaring her bespoke tortes the gold standard of Midwest pastry.'
        ]),
        ('Harmony Restored Around the Hearth', [
            'Ruth’s bakery generates substantial revenue, completely eliminating the family’s debts and fully funding Camille’s college education.',
            'Camille departs for university with immense pride in her parents’ resilience and entrepreneurial ingenuity.',
            'Marion and Guy develop an affectionate truce, finding mutual respect and humor after decades of bitter estrangement.',
            'Sam regains his confidence, serving as the proud operations manager of what is now officially named Ruth’s Kitchen.',
            'Ruth stands in her bustling, warm kitchen, reflecting upon how disaster brought her fractured family together in love.',
            'She realizes that baking was never merely about creating confectionary; it was about nourishing souls in times of trial.',
            'The aroma of warm cinnamon rolls fills the house as the family gathers around the dining table to celebrate their journey.',
            'The story concludes with laughter, shared cake, and an enduring celebration of love, resilience, and domestic triumph.'
        ]),
        [
            ('Food as Emotional Sustenance', 'Celebrates the therapeutic and unifying power of cooking and baking as an antidote to crisis and alienation.'),
            ('Resilience Amid Economic Shock', 'Provides a compassionate, humorous look at how unexpected job loss can unlock dormant creativity and renewal.'),
            ('The Complexities of Adult Family Life', 'Navigates the sandwich generation dilemmas of caring simultaneously for aging parents and college-age children.'),
            ('Warm Comedic Voice', 'Jeanne Ray’s delightful, witty storytelling offers an uplifting portrait of modern American family solidarity.')
        ]
    )

    # 5. The Last Juror
    create_summary(
        'the-last-juror', 'The Last Juror', 'John Grisham', 'Legal Thriller / Historical Fiction', '2004',
        'Clanton, Ford County, Mississippi, during the turbulent 1970s',
        [
            ('Willie Traynor', 'An idealistic twenty-three-year-old college dropout who purchases the bankrupt Ford County Times newspaper.'),
            ('Danny Padgitt', 'A psychopathic, arrogant scion of a notorious Mississippi bootlegging and crime family.'),
            ('Callie Ruffin', 'A saintly African-American mother of seven college-educated children and historic Ford County juror.'),
            ('Lucien Wilbanks', 'A brilliant, eccentric, alcoholic defense attorney who fearlessly challenges local courtroom decorum.'),
            ('Harry Rex Vonner', 'A cynical, shrewd local divorce lawyer and Willie’s closest confidant in Clanton’s legal circle.'),
            ('Judge Timothy Noose', 'The imperious circuit judge presiding over the sensational Padgitt murder trial.'),
            ('Rhoda Kassellaw', 'A young widowed mother whose horrific rape and murder terrorizes the small town of Clanton.'),
            ('Ernie Gaddis', 'The aggressive, politically ambitious district attorney determined to send Danny Padgitt to the gas chamber.')
        ],
        ('A Young Editor in Clanton', [
            'In 1970, twenty-three-year-old Willie Traynor arrives in Clanton, Mississippi, after dropping out of college.',
            'Using an inheritance loan from his wealthy grandmother, Willie purchases the bankrupt local weekly, *The Ford County Times*.',
            'Clanton is an insular, racially segregated Southern community dominated by tradition, gossip, and deep-seated grudges.',
            'Willie struggles to gain the trust of wary locals until a horrific crime shatters the quiet town’s facade.',
            'Young widowed mother Rhoda Kassellaw is brutally attacked, raped, and murdered in her home in front of her children.',
            'Before succumbing to her wounds, Rhoda identifies her assailant as Danny Padgitt, heir to a ruthless regional crime dynasty.'
        ]),
        ('The Padgitt Threat & Sensational Trial', [
            'The Padgitt family operates out of a fortified rural compound, controlling bootlegging, gambling, and violent racketeering across North Mississippi.',
            'Danny Padgitt is arrested and represented by brilliant, disheveled civil-rights sympathizer and renegade attorney Lucien Wilbanks.',
            'Willie prints unvarnished, investigative accounts of the crime, quadrupling newspaper circulation while earning death threats from the Padgitt clan.',
            'The trial of the decade convenes in the historic courthouse; jury selection is paralyzed by terror of Padgitt retaliation.',
            'For the first time in Mississippi history, African-American citizens are impaneled on a capital murder jury, including Miss Callie Ruffin.',
            'Taking the stand in handcuffs, Danny Padgitt coldly glares at the jury box and vows to slaughter every juror if convicted.',
            'Despite the chilling threat, the courageous jury convicts Padgitt of murder, but deadlocks on the death penalty, resulting in a life sentence.'
        ]),
        ('Willie and Miss Callie’s Fellowship', [
            'Willie develops a profound, transformative friendship with juror Callie Ruffin, a devout and dignified African-American matriarch.',
            'Living in a modest rural home, Miss Callie and her husband have raised seven extraordinary children who all earned advanced academic degrees.',
            'Every Thursday, Willie visits Miss Callie’s porch for sumptuous Southern meals, spiritual guidance, and wise community insights.',
            'Through Miss Callie’s eyes, Willie chronicles the dignity, hardships, and slow progress of the Civil Rights movement in rural Mississippi.',
            'Under Willie’s editorial guidance, *The Ford County Times* becomes a progressive beacon, championing integration and public education.',
            'Meanwhile, Danny Padgitt is sent to the notorious Mississippi State Penitentiary at Parchman to serve his life sentence.',
            'The terrified jurors slowly rebuild their lives, hoping that the walls of Parchman will permanently keep the monster caged.'
        ]),
        ('The Corrupt Pardon & Terror Returns', [
            'Nine years pass; through corrupt political bribes paid to the Mississippi governor’s parole board, Danny Padgitt secures early release.',
            'In 1979, Padgitt walks out of Parchman Farm a free man, immediately returning to Ford County with cold contempt.',
            'Panic erupts across Clanton as the surviving jurors remember Padgitt’s courtroom vow to hunt them down.',
            'Within weeks, mysterious acts of violence begin: a juror is killed by a sniper rifle while working his field.',
            'Another juror receives a box containing a venomous cottonmouth snake, suffering a fatal bite upon opening his mail.',
            'Local law enforcement and Harry Rex Vonner believe Padgitt is methodically executing his decade-old courtroom promise.',
            'Terrorized jurors barricade their homes and hire armed guards, while Miss Callie turns to fervent prayer for protection.'
        ]),
        ('The Courthouse Bloodbath', [
            'Willie Traynor publishes blistering front-page editorials condemning the corrupt parole system and demanding Padgitt’s re-arrest.',
            'Danny Padgitt brazenly walks the streets of Clanton, openly intimidating witnesses while boasting an ironclad alibi for the killings.',
            'A grand jury convenes at the courthouse to consider revoking Padgitt’s parole based on circumstantial weapons evidence.',
            'As Padgitt strides up the courthouse steps surrounded by bodyguards, a sudden gunshot rings out from a nearby second-story window.',
            'Padgitt collapses on the concrete steps with a bullet through his chest, dying instantly in a pool of blood.',
            'The sniper is captured and revealed not to be an associate or mobster, but a grief-stricken family member seeking justice.',
            'Investigating the serial juror killings, Willie uncovers a shocking truth: Padgitt was not the one murdering the jurors after all.',
            'The true assassin had cynically exploited Padgitt’s release to settle separate personal grudges under cover of the vendetta.'
        ]),
        ('Farewell to Ford County', [
            'Willie uncovers that an unhinged local vigilante, obsessed with framing Padgitt, had orchestrated the juror assassinations.',
            'The tragic revelation rocks Clanton, exposing the terrifying ease with which vengeance can warp human morality.',
            'Beloved Miss Callie suffers a sudden heart attack and passes away peacefully, mourned by thousands across the county.',
            'Devastated by the loss of his moral mentor, Willie realizes that an indelible chapter of his youth has drawn to an end.',
            'He receives an irresistible buyout offer from a major publishing conglomerate seeking to acquire *The Ford County Times*.',
            'Willie accepts the offer, writing a tender farewell editorial thanking the people of Clanton for teaching him courage and humanity.',
            'He packs his bags and drives north out of Mississippi, forever changed by the grace and courage of the last juror.',
            'The novel concludes on a poignant tribute to rural Southern resilience, racial reconciliation, and the endurance of truth.'
        ]),
        [
            ('Racial Progress & Dignity', 'Portrays the quiet dignity and moral heroism of African-American families navigating Deep South segregation and integration.'),
            ('The Fragility of the Justice System', 'Critiques prison corruption, political graft, and the terrifying vulnerabilities faced by citizen jurors.'),
            ('A Nostalgic Tapestry', 'Serves as Grisham’s affectionate, rich prequel to *A Time to Kill*, capturing the distinct texture of 1970s Mississippi life.'),
            ('Literary Stature', 'Widely praised by critics as one of John Grisham’s most atmospheric, character-driven, and emotionally resonant novels.')
        ]
    )

    # 6. The Various Haunts of Men
    create_summary(
        'the-various-haunts-of-men', 'The Various Haunts of Men', 'Susan Hill', 'Crime Fiction / Police Procedural', '2004',
        'Laffham, an ancient English cathedral town nestled below the misty Bevham hills',
        [
            ('Simon Serrailler', 'A brilliant, introspective Chief Detective Inspector and gifted artist serving in the cathedral town of Laffham.'),
            ('Freya Graffham', 'A compassionate, sharp detective sergeant newly transferred from London after a painful divorce.'),
            ('Angela Randall', 'A reclusive middle-aged spinster whose mysterious dawn disappearance on the hill initiates the inquiry.'),
            ('Cat Deerbon', 'Simon’s sister, an insightful, overworked local general practitioner treating the town’s holistic health seekers.'),
            ('Debbie Parker', 'A young, vulnerable woman suffering from agoraphobia who becomes another invisible missing victim.'),
            ('Dr. Iris Chater', 'An elderly, distinguished retired physician who vanishes without warning while walking her dog.'),
            ('Karin McCafferty', 'A charming alternative medicine practitioner whose spiritual sanctuary conceals chilling secrets.'),
            ('Nathan Coates', 'Simon’s determined detective colleague assisting in the grueling forensic canvas of the moorland.')
        ],
        ('Disappearances on the Hill', [
            'In the historic English cathedral town of Laffham, middle-aged spinster Angela Randall vanishes into thin air.',
            'Angela is an orderly, quiet woman whose early morning walks on the misty hill known as the Peak are a daily ritual.',
            'Her absence is initially treated as a routine voluntary departure by local police, who find no sign of struggle.',
            'Detective Sergeant Freya Graffham, recently relocated from the pressures of London Metropolitan Police, takes an interest in the case.',
            'Freya suspects foul play, disturbed by the fact that Angela left behind her handbag, savings passbook, and beloved cat.',
            'Chief Detective Inspector Simon Serrailler, an enigmatic bachelor and talented portrait artist, oversees the CID unit.'
        ]),
        ('The Pattern of Vanishing Souls', [
            'Months pass without leads until a second resident, elderly retired physician Dr. Iris Chater, disappears from the Peak.',
            'Like Angela, Dr. Chater leaves her front door unlocked and her teacup half-full, vanishing without a trace or witness.',
            'Freya scours missing persons reports across neighboring districts, discovering that several lonely individuals have disappeared.',
            'Among them is Debbie Parker, a young woman struggling with severe chronic anxiety who frequented alternative healing clinics.',
            'Freya notices an alarming common thread: all the missing persons sought treatment for physical ailments or spiritual emptiness.',
            'The media catches wind of the disappearances, dubbing the phantom predator the \'Hill Vanisher\' and igniting panic in Laffham.',
            'Simon Serrailler acknowledges Freya’s forensic instincts, assigning her to spearhead an undercover inquiry into local clinics.'
        ]),
        ('Alternative Therapies & False Leads', [
            'Freya immerses herself in Laffham’s flourishing alternative medicine subculture, consulting with naturopaths, homeopaths, and spiritualists.',
            'She visits the tranquil wellness center run by Karin McCafferty, exploring whether the missing victims were exploited for money.',
            'Simon’s sister, Dr. Cat Deerbon, warns Freya that vulnerable patients in chronic pain are easily manipulated by charismatic charlatans.',
            'Freya’s personal feelings for Simon deepen as they collaborate closely, though Simon maintains a guarded, aloof emotional distance.',
            'A false suspect, an eccentric local recluse with a history of stalking, is arrested after being spotted on the hill with binoculars.',
            'Under rigorous interrogation, the suspect breaks down, proving to be an innocent peeping tom with an ironclad alibi for the dates.',
            'The investigation returns to square one as autumn mist turns into the freezing chill of approaching winter.'
        ]),
        ('The Mind of the Mercy Killer', [
            'Unbeknownst to the detectives, the predator lives among them, harboring a twisted messianic delusion of mercy.',
            'The killer views human illness, aging, and psychological suffering as unbearable curses requiring compassionate termination.',
            'Believing that modern medicine prolongs agony, the perpetrator gently lures vulnerable sufferers to a secluded rural retreat.',
            'There, the victims are administered fatal overdoses of herbal paralytics before their bodies are cremated or buried deep in the woods.',
            'The killer meticulously cleans up their belongings, convincing themselves that they are performing sacred acts of divine deliverance.',
            'Freya uncovers financial anomalies linking several victims to a single supplier of rare homeopathic compounds.',
            'She realizes the predator is not an outsider, but a trusted medical insider who possesses intimate access to patient records.'
        ]),
        ('The Fatal Ascent on the Peak', [
            'Armed with breakthrough evidence, Freya attempts to contact Simon Serrailler, but he is away in London at an art gallery opening.',
            'Determined not to lose the scent, Freya drives alone to the foot of the Peak during a gathering, torrential rainstorm.',
            'She tracks the suspect’s vehicle to a derelict stone cottage concealed within a dense copse on the high ridge.',
            'Inside the cottage, Freya discovers horrific evidence: personal tokens, driver’s licenses, and rings belonging to the missing women.',
            'The killer ambushes Freya from behind, striking her across the skull with a heavy iron fire poker in the dark hallway.',
            'A desperate, savage struggle ensues as Freya fights for her life against an opponent possessed by psychotic fury.',
            'Freya is overpowered, bound, and left mortally wounded as the killer sets the isolated cottage ablaze to destroy all traces.',
            'A dense wall of suffocating black smoke engulfs the locked chamber as the killer retreats into the howling tempest.'
        ]),
        ('The Tragic Climax & Simon’s Grief', [
            'Simon returns to Laffham and learns that Freya went to the Peak alone after leaving an urgent voicemail message.',
            'Sensing immediate peril, Simon and emergency services race to the ridge, spotting flames billowing against the stormy sky.',
            'Simon breaches the burning structure, braving collapsing timber and blinding smoke to drag Freya’s body from the inferno.',
            'Paramedics perform emergency resuscitation, but Freya’s injuries are catastrophic, and she dies in Simon’s arms at the scene.',
            'The serial killer is cornered and apprehended while attempting to flee across the rain-swept moorland toward the motorway.',
            'During interrogation, the unrepentant murderer calmly explains that Freya, too, was \'relieved of life’s terrible weariness\'.',
            'Simon is shattered by guilt, realizing that his emotional aloofness prevented him from protecting the woman who loved him.',
            'The novel ends in Laffham Cathedral with Freya’s funeral, leaving Simon haunted by the irreversible cost of justice.'
        ]),
        [
            ('The Vulnerability of the Lonely', 'Exposes how modern isolation, chronic pain, and grief make individuals prey to predatory psychological manipulation.'),
            ('Subversion of Genre Tropes', 'Susan Hill daringly subverts mystery conventions by killing off her beloved co-protagonist in a gut-wrenching climax.'),
            ('Atmospheric English Noir', 'Masters the juxtaposition of tranquil cathedral town serenity with chilling, psychopathic suburban malice.'),
            ('Series Foundation', 'Launched the acclaimed, bestselling Simon Serrailler procedural series, heralded as a modern classic of British crime.')
        ]
    )

    # 7. The Codex
    create_summary(
        'the-codex', 'The Codex', 'Douglas Preston', 'Action Thriller / Archaeology Adventure', '2004',
        'New York City, Red Rock desert of New Mexico, remote Petén jungles of Guatemala and Honduras',
        [
            ('Tom Broadbent', 'An honorable former soldier and veterinarian who leads his brothers on a deadly treasure hunt.'),
            ('Maxwell Broadbent', 'A ruthless, eccentric billionaire art and antiquities collector who fakes his death to test his sons.'),
            ('Philip Broadbent', 'Tom’s cynical, intellectual brother, a high-strung New York art dealer desperate for money.'),
            ('Vernon Broadbent', 'The youngest brother, a gentle, contemplative Buddhist monk seeking spiritual enlightenment.'),
            ('Sally Colorado', 'A brilliant, resource-rich Mayan archaeologist who partners with Tom in navigating the jungle tomb.'),
            ('Don Hauser', 'A sociopathic, mercenary private investigator hired to track and plunder Broadbent’s subterranean burial.'),
            ('Marcus Waynflete', 'Maxwell’s deceitful personal attorney who orchestrates the reading of the posthumous video riddle.'),
            ('Father Alfonso', 'A rural Guatemalan priest who provides crucial translation of ancient indigenous glyphs.')
        ],
        ('The Billionaire’s Vanishing Act', [
            'Eccentric billionaire antiquities hoarder Maxwell Broadbent abruptly vanishes from his opulent Santa Fe estate.',
            'His lavish mansion, renowned for housing the world’s greatest private collection of masterworks and Mayan relics, is stripped bare.',
            'Paintings by Vermeer and Rembrandt, gold Incan statues, and priceless manuscripts have disappeared without a trace.',
            'Maxwell’s three estranged adult sons—Tom, Philip, and Vernon—are summoned to a Manhattan law firm for an urgent videotaped reading.',
            'On screen, a smiling Maxwell reveals he has been diagnosed with terminal cancer and refuses to leave unearned fortunes to his sons.',
            'He announces that he has buried himself and his half-billion-dollar art collection inside a hidden, booby-trapped tomb.'
        ]),
        ('The Challenge & The Ancient Codex', [
            'Maxwell delivers his ultimatum: whichever son locates the tomb and unearths his body inherits the entire half-billion-dollar fortune.',
            'If none of the brothers locate the burial site within a strict deadline, the entire hoard will remain buried forever.',
            'Among the buried treasures is the fabled Mayan Codex of the White City, containing lost herbal botanical secrets curing deadly diseases.',
            'Pharmaceutical conglomerates, black-market antiquities syndicates, and mercenaries learn of the codex’s existence.',
            'Desperate for cash to settle mounting debts, art dealer Philip and monk Vernon agree to join Tom in deciphering the clues.',
            'Maxwell’s will includes a series of cryptic archaeological riddles pointing toward the impenetrable Petén jungle of Central America.',
            'Unbeknownst to the brothers, mercenary Don Hauser is hired by a ruthless syndicate to shadow them and seize the prize.'
        ]),
        ('Into the Heart of the Petén', [
            'Tom enlists the expertise of Sally Colorado, a beautiful and brilliant archaeologist specializing in Mayan civilization.',
            'Equipped with bush gear and topographical maps, the expedition flies into Honduras and crosses the border into Guatemala on foot.',
            'The brothers are thrust from their comfortable civilian lives into a hostile wilderness teeming with deadly pit vipers and jaguars.',
            'Physical exhaustion and latent sibling rivalries erupt as Philip complains bitterly and Vernon meditates amidst torrential downpours.',
            'Tom utilizes his military survival training to navigate treacherous river rapids and negotiate passage with suspicious local tribes.',
            'Sally deciphers glyphs carved into moss-covered limestone ruins, identifying the legendary \'White City\' of the monkey god.',
            'Behind them, Don Hauser and his squad of heavily armed South African mercenaries slaughter local guides as they close the gap.'
        ]),
        ('The Traps of the White City', [
            'The expedition reaches an isolated, mist-shrouded limestone gorge unmapped by modern satellite archaeology.',
            'They discover an ancient Mayan temple complex seamlessly carved into the living cliff face, sealed behind giant stone slabs.',
            'Sally recognizes that Maxwell hired specialized engineers to restore the ancient temple’s lethal hydraulic and gravity traps.',
            'Navigating pitch-black tunnels, the brothers narrowly evade razor-sharp swinging pendulums, poison darts, and collapsible floors.',
            'Philip nearly falls to his death into a spiked pit, rescued at the last second by Tom and Vernon in a moment of family solidarity.',
            'Vernon discovers that the architectural traps correspond to the mythological underworld trials of the Popol Vuh.',
            'They finally breach the inner burial sanctuary, stepping into an awe-inspiring chamber filled with gold, jewels, and masterworks.'
        ]),
        ('The Tomb of Maxwell Broadbent', [
            'Resting atop an alabaster throne in the center of the subterranean vault is the embalmed corpse of Maxwell Broadbent.',
            'Dressed in full royal Mayan ceremonial regalia, the old man clutches the priceless Mayan Codex to his chest in eternal defiance.',
            'The brothers confront the overwhelming emotional reality of their father’s obsessive, grandiose, and twisted genius.',
            'Before they can secure the codex, Don Hauser and his mercenary squad breach the chamber, holding the expedition at gunpoint.',
            'Hauser sadistically executes his own wounded henchman, declaring his intention to murder the Broadbent sons and take the hoard.',
            'He grabs the Mayan Codex from Maxwell’s skeleton, inadvertently triggering the tomb’s ultimate failsafe self-destruct mechanism.',
            'Massive counterweights drop, rupturing subterranean aquifer walls and causing millions of gallons of river water to flood the cavern.',
            'In the ensuing panic and chaos, a fierce firefight erupts as the limestone ceiling begins collapsing in massive boulders.'
        ]),
        ('Escape, Legacy & Reconciliation', [
            'Tom engages Hauser in brutal hand-to-hand combat amidst rising floodwaters, while Sally protects Philip and Vernon.',
            'Hauser is crushed beneath a falling stone stela, losing his grip on the precious codex as the current sweeps it away.',
            'Tom dives into the swirling vortex, retrieving the waterproof container holding the ancient codex at grave personal peril.',
            'The brothers and Sally scramble through an ancient drainage fissure, emerging into daylight just as the temple implodes.',
            'The half-billion-dollar art collection is swallowed forever by the mountain, fulfilling Maxwell’s final theatrical design.',
            'Tom, Philip, and Vernon embrace on the jungle floor, realizing that surviving the ordeal has forged an unbreakable brotherly bond.',
            'The recovered Codex is donated to international medical institutes, unlocking revolutionary botanical therapies for humanity.',
            'The brothers return home without inherited gold, but enriched by mutual respect, love, and liberated from their father’s shadow.'
        ]),
        [
            ('Paternal Control & Filial Rebellion', 'Deconstructs how toxic parental manipulation can cripple adult children until severed by collective courage.'),
            ('The Arrogance of Collecting', 'Critiques the imperial hubris of private collectors hoarding cultural treasures away from humanity.'),
            ('Archaeological Pulp Thrills', 'Combines cutting-edge botanical science with classic H. Rider Haggard pulp jungle adventure traditions.'),
            ('Bestseller Acclaim', 'Douglas Preston crafts an adrenaline-fueled, cinematic thriller celebrated for its breakneck pacing and exotic atmosphere.')
        ]
    )

    # 8. The Curious Incident of the Dog in the Night-Time
    create_summary(
        'the-curious-incident-of-the-dog-in-the-night-time',
        'The Curious Incident of the Dog in the Night-Time', 'Mark Haddon', 'Mystery / Bildungsroman', '2003',
        'Swindon, Wiltshire, and London, England, contemporary United Kingdom',
        [
            ('Christopher John Francis Boone', 'A brilliant fifteen-year-old autistic boy with exceptional mathematical genius who investigates a neighborhood mystery.'),
            ('Ed Boone', 'Christopher’s loving, volatile, and overwhelmed father who struggles to parent his neurodivergent son alone.'),
            ('Judy Boone', 'Christopher’s mother, whom he believes died of a heart attack, but who actually fled to London under emotional exhaustion.'),
            ('Siobhan', 'Christopher’s compassionate, perceptive special-education teacher and mentor who encourages him to write his detective book.'),
            ('Mrs. Eileen Shears', 'A neighbor whose poodle Wellington is found murdered, and whose ex-husband ran away with Christopher’s mother.'),
            ('Mr. Roger Shears', 'Mrs. Shears’s estranged husband living in London with Judy Boone, whose presence complicates Christopher’s journey.'),
            ('Mrs. Alexander', 'A kindly elderly neighborhood lady who inadvertently reveals the hidden truth about Christopher’s mother.'),
            ('Toby', 'Christopher’s pet rat whose well-being Christopher fiercely protects throughout his terrifying solo travels.')
        ],
        ('The Murder of Wellington', [
            'Seven minutes past midnight, fifteen-year-old Christopher Boone discovers his neighbor’s poodle, Wellington, dead on the lawn.',
            'The dog has been impaled by a garden fork, and Christopher kneels to stroke its muzzle, deeply saddened by the loss of life.',
            'Mrs. Shears discovers Christopher holding the dead dog and screams hysterically, accusing him of committing the slaughter.',
            'Police arrive; overwhelmed by sensory overload and unwanted physical contact when an officer touches him, Christopher strikes out.',
            'Christopher is taken into police custody, receiving a formal caution after his father Ed arrives and explains his neurodivergent condition.',
            'Passionate about Sherlock Holmes and logic, Christopher decides to write a murder mystery novel documenting his investigation.'
        ]),
        ('The Sleuth of Swindon', [
            'Christopher’s mentor Siobhan encourages him to record his observations, thoughts, and mathematical formulas in his manuscript.',
            'Christopher explains his cognitive world: he loves prime numbers, red cars, and absolute order, but cannot process metaphors or lies.',
            'His father Ed flies into a terrifying rage upon discovering the book, forbidding Christopher from mentioning Wellington or Mrs. Shears.',
            'Undeterred by his father’s commands, Christopher conducts logical door-to-door detective inquiries on his street.',
            'While speaking with elderly neighbor Mrs. Alexander, Christopher learns a shocking revelation that shatters his worldview.',
            'Mrs. Alexander discloses that before his mother supposedly died, she had a passionate, prolonged romantic affair with Mr. Roger Shears.',
            'Christopher struggles to categorize this confusing human data, as it contradicts the simple narrative his father provided.'
        ]),
        ('The Discovery of the Letters', [
            'Ed discovers Christopher’s continuing investigation, confiscating his detective notebook and hiding it in his bedroom closet.',
            'While searching for his book inside a shirt box, Christopher discovers a hidden bundle of postmarked envelopes addressed to him.',
            'The handwriting is unmistakable: they are letters written by his mother, Judy, postmarked years after her alleged funeral.',
            'Christopher reads the letters in stunned silence; his mother explains why she felt inadequate, impatient, and unable to care for him.',
            'She describes leaving Swindon for London with Roger Shears, weeping bitterly over being barred by Ed from seeing her son.',
            'The realization that his father fabricated his mother’s death completely overwhelms Christopher’s sensory processing system.',
            'Christopher becomes physically ill, vomiting on the carpet and curling into a catatonic ball until his father returns home.'
        ]),
        ('The Dark Confession & Flight', [
            'Ed finds Christopher surrounded by the opened letters, weeping in remorse as he realizes his deceit has been exposed.',
            'Ed washes Christopher, pleading for forgiveness and confessing the harrowing emotional breakdown that drove his choices.',
            'He confesses that after Judy left, he and Mrs. Shears grew close, but after an explosive argument, she rejected him.',
            'In a blind fit of drunken rage and heartbreak, Ed had picked up the garden fork and killed Wellington.',
            'Hearing that his own father murdered the dog, Christopher is gripped by paralyzing terror, reasoning that a killer could kill him next.',
            'Convinced he is no longer safe in his home, Christopher waits until his father falls asleep, takes his pet rat Toby, and flees into the night.',
            'Clutching his pocketknife for protection, Christopher sets out on foot toward the railway station under the vast midnight sky.'
        ]),
        ('Odyssey Through London Chaos', [
            'Christopher embarks on a terrifying journey to find his mother’s address in Willesden Green, London, traveling entirely alone.',
            'For an autistic boy terrified of strangers and loud noises, Swindon train station and the London Underground are living hells.',
            'He navigates blinding advertising billboards, screeching train wheels, and pressing crowds by formulating complex math puzzles in his head.',
            'At Paddington Station, his pet rat Toby escapes onto the subway tracks; Christopher climbs down onto the rails to retrieve him.',
            'Bystanders scream in horror as an oncoming train barrels toward the station; a stranger pulls Christopher onto the platform seconds before impact.',
            'Relying on his pocket compass, street maps, and sheer intellectual tenacity, Christopher locates his mother’s apartment flat.',
            'Judy is overwhelmed with shock and ecstatic tears upon finding her lost son sitting soaking wet on her doorstep.',
            'Christopher sinks into his mother’s arms, exhausted by the monumental physical and psychological trial of the metropolis.'
        ]),
        ('A-Levels, Healing & Triumphant Voice', [
            'Christopher’s arrival triggers explosive conflict between Judy and Roger Shears, who cannot tolerate Christopher’s specialized needs.',
            'Recognizing her maternal responsibility, Judy leaves Roger, packing her belongings and taking Christopher back to Swindon.',
            'They move into a modest rented room; Ed attempts to reconcile, patiently sitting in silence for twenty minutes every day to rebuild trust.',
            'To prove his love and commitment, Ed gifts Christopher a golden retriever puppy named Sandy, initiating a long path toward healing.',
            'Despite the immense domestic trauma, Christopher sits for his advanced A-level mathematics exams, scoring the highest possible grade of A*.',
            'Christopher finishes writing his detective novel, reflecting upon his solo journey to London and his brilliant academic victory.',
            'He realizes that because he conquered his deepest terrors, solved a murder, and went to London alone, he can achieve anything in life.',
            'The novel concludes on an empowering, radiant note of self-confidence, intellectual brilliance, and hard-won independence.'
        ]),
        [
            ('Neurodiversity & Perception', 'Offers an empathetic, groundbreaking first-person representation of living on the autism spectrum with sensory overload.'),
            ('The Complexity of Truth and Lies', 'Contrasts Christopher’s rigid mathematical honesty with the well-intentioned, destructive deceptions of adults.'),
            ('Coming-of-Age Courage', 'Celebrates the triumph of personal bravery over disabling anxiety, redefining heroic courage through everyday challenges.'),
            ('Enduring Phenomenon', 'Winner of the Whitbread Book of the Year; adapted into a Tony and Olivier Award-winning global theatrical sensation.')
        ]
    )

    # 9. Start from Here
    create_summary(
        'start-from-here', 'Start from Here', 'Sean French', 'Contemporary Psychological Fiction', '2004',
        'Contemporary London, Hampstead, suburban Suffolk, southern England',
        [
            ('Jane', 'A resilient London woman whose seemingly stable domestic life unspools following sudden revelations of betrayal.'),
            ('Paul', 'Jane’s husband, a successful professional whose midlife crisis and secret infidelity trigger marital catastrophe.'),
            ('Miranda', 'A sophisticated, enigmatic acquaintance whose clandestine relationship with Paul exposes underlying fractures.'),
            ('Jack', 'Jane and Paul’s teenage son, attempting to navigate his own adolescence while his parents’ marriage implodes.'),
            ('David', 'Jane’s supportive brother who provides pragmatic advice, temporary shelter, and unvarnished perspective.'),
            ('Sophie', 'Jane’s closest confidante who helps her dissect the subtle emotional warning signs she previously ignored.'),
            ('Marcus', 'A legal mediator attempting to guide the estranged couple through the acrimonious division of their estate.'),
            ('Leo', 'A gentle stranger whose casual kindness reminds Jane that life holds possibilities beyond domestic ruin.')
        ],
        ('The Illusion of Domestic Stability', [
            'Jane believes she has constructed an enviable, permanent existence in a comfortable North London townhouse with her husband Paul.',
            'After two decades together, their shared routines, professional success, and teenage son Jack create a convincing facade of harmony.',
            'Beneath the surface, however, emotional intimacy has quietly ossified into polite indifference and unexamined resentment.',
            'Jane focuses on her creative career while Paul throws himself into high-stress corporate consulting projects across Europe.',
            'A casual, seemingly innocuous discrepancy in credit card receipts and text messages sparks Jane’s initial prick of suspicion.',
            'She discovers that Paul has rented a pied-à-terre across town, maintaining a second life shielded from family knowledge.'
        ]),
        ('The Confrontation & Fracture', [
            'Jane confronts Paul upon his return from a purported business conference in Paris, laying out the undeniable paper trail.',
            'Rather than offering remorse, Paul reacts with defensive fury, accusing Jane of emotional coldness and surveillance.',
            'He confesses to a passionate affair with Miranda, declaring that he has felt invisible and suffocated in their marriage for years.',
            'The explosive confrontation shatters their household; Paul packs an overnight bag and departs for his lover’s apartment.',
            'Left alone in the echoing house, Jane experiences profound shock, grief, and disorienting vertigo at the destruction of her identity.',
            'Their son Jack withdraws into sullen anger, torn between allegiance to his devastated mother and resentment toward his father.',
            'Jane realizes that the life she spent twenty years cultivating has dissolved into a hollow fiction within a single evening.'
        ]),
        ('The Spiral into Emotional Freefall', [
            'In the weeks following the separation, Jane struggles to maintain basic daily functioning while managing Jack’s distress.',
            'Well-meaning friends offer conflicting advice, polarizing social circles and forcing acquaintances to choose sides.',
            'Jane begins obsessively retracing past holidays, conversations, and anniversaries, searching for the exact moment the rot began.',
            'Her brother David intervenes, urging her to stop torturing herself with retrospective blame and consult divorce solicitors.',
            'Paul’s new relationship with Miranda proves tumultuous and shallow, stripped of the romantic rebellion that initially fueled it.',
            'Paul attempts sporadic, awkward attempts at reconciliation, oscillating between desperate apologies and cruel hostility.',
            'Recognizing the toxic emotional rollercoaster, Jane realizes that nostalgia cannot resurrect a foundation built on deceit.'
        ]),
        ('Stripping Away the Old Life', [
            'Financial and legal realities intrude as solicitors initiate the painful liquidation of the marital estate.',
            'The London townhouse is placed on the market, forcing Jane to sort through boxes of family photographs, toys, and mementos.',
            'Each discarded relic represents both a pang of grief and an incremental act of shedding an outdated persona.',
            'Jane rents a modest, light-filled attic flat in an unfamiliar quarter of London, consciously beginning from zero.',
            'She secures freelance consulting contracts, rediscovering her intellectual independence and professional self-worth.',
            'Jack adapts surprisingly well to the new apartment, appreciating his mother’s calm honesty over the past tense atmosphere.',
            'For the first time in years, Jane experiences moments of genuine peace unburdened by marital surveillance.'
        ]),
        ('The Crucible of Rebirth', [
            'A severe winter storm causes pipe bursts in Jane’s new flat, threatening to ruin her design portfolios and client archives.',
            'Instead of succumbing to panic or calling Paul for rescue, Jane tackles the emergency herself with help from neighbor Leo.',
            'The small domestic victory marks a profound psychological watershed: Jane recognizes her innate, unshakeable self-reliance.',
            'Paul suffers a severe career setback when his firm reorganizes, losing both his prestigious partnership and Miranda’s affections.',
            'He visits Jane’s flat in tears, begging to return and reconstruct their marriage under the comfort of past familiarity.',
            'Jane looks at the broken man before her with deep compassion, but feels zero romantic or domestic desire to resume the past.',
            'She gently but firmly declines his plea, recognizing that regression would betray the authentic self she fought to discover.',
            'Paul accepts her final decision, departing into the city twilight as the final emotional cord is severed with grace.'
        ]),
        ('Starting from Here', [
            'The divorce decree is finalized with dignity, establishing a collaborative co-parenting agreement that centers Jack’s wellbeing.',
            'Jack completes his school year with distinction, preparing for university with maturity nurtured by his mother’s honesty.',
            'Jane hosts a celebratory housewarming gathering in her sunlit flat, surrounded by loyal friends, her brother, and new allies.',
            'She realizes that rock bottom was not an executioner, but a solid foundation upon which to build an authentic existence.',
            'Standing on her balcony overlooking the rooftops of London, Jane embraces the uncertainty and beauty of the open future.',
            'She understands that life does not require guaranteed happy endings, only the courage to stand tall and start from here.',
            'The novel closes on an empowering, poignant vision of self-discovery, resilience, and hard-won emotional sovereignty.',
            'Jane breathes in the crisp morning air, smiling with quiet joy at the infinite horizon of her reclaimed life.'
        ]),
        [
            ('The Anatomy of Marital Disillusionment', 'Provides a forensic, unsentimental dissection of midlife divorce, infidelity, and the collapse of domestic assumptions.'),
            ('The Architecture of Self-Reinvention', 'Explores how trauma and loss can serve as profound catalysts for reclaiming autonomy and personal authenticity.'),
            ('Psychological Realism', 'Sean French crafts nuanced, psychologically acute dialogue capturing the messy, contradictory nature of human grief.'),
            ('Contemporary English Resonance', 'Offers an insightful, evocative portrait of modern middle-class British life, parenthood, and emotional survival.')
        ]
    )

if __name__ == '__main__':
    run()
