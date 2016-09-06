db.createCollection("phases")

db.phases.insert({
    phase_title: "INBOX",
    phase_order: 1,
    node_list: [
        "Default","GMail","Work Outlook","Weber Email", "Recurring Tasks", "Web Clips"
        ] 
})

db.phases.insert({
    phase_title: "TRIAGE",
    phase_order: 2,
    node_list: [
        "Home Triage","Work Triage","School Triage"
    ]
})

db.phases.insert({
    phase_title: "REFERENCE",
    phase_order: 3,
    node_list: [
        "Programming References","Career References","Domestic References","Physical References","Mental/Spiritual References"
    ]
})

db.phases.insert({
    phase_title: "PROJECTS",
    phase_order: 4,
    node_list: [
        "Dormant Project","Incubative Projects","Active Home Projects","Active Work Projects","Active School Projects"
    ]
})

db.phases.insert({
    phase_title: "TIME BASED",
    phase_order: 5,
    node_list: [
        "Upcoming this Year","Upcoming this Month","Upcoming this Week","Upcoming Ubermorgen","Upcoming Tomorrow","Todays Backlog"
    ]
})

db.phases.insert({
    phase_title: "KANBAN",
    phase_order: 6,
    node_list: [
        "Current Focus","Completed Today","Completed this Week"
    ]
})





