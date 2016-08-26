
/* PHASES ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*/
CREATE TABLE PHASE(
    phase_id			TINYINT UNSIGNED		PRIMARY KEY	NOT NULL,
    phase_title		    VARCHAR(20) 		    NOT NULL,
    default_bool    	BOOLEAN     	        NOT NULL
);
#INSERT INTO PHASES VALUES (phase_id, phase_title, default_bool)
INSERT INTO PHASE VALUES (null, 'INBOX', TRUE);
INSERT INTO PHASE VALUES (null, 'TRIAGE', FALSE);
INSERT INTO PHASE VALUES (null, 'REFERENCE', FALSE)
INSERT INTO PHASE VALUES (null, 'PROJECTS', FALSE);
INSERT INTO PHASE VALUES (null, 'KANBAN', FALSE);


/* NODES ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ */
CREATE TABLE NODE(
    node_id 			SMALLINT UNSIGNED	PRIMARY KEY	NOT NULL,
    node_title		    VARCHAR(20) 		NOT NULL,
    phase_id            SMALLINT UNSIGNED   NOT NULL,
    default_bool    	BOOLEAN     	    NULL,
    FOREIGN KEY(phase_id) REFERENCES PHASE(phase_id)
);
#INSERT INTO NODES VALUES (node_id, node_title, phase_id, visible_bool) 
INSERT INTO NODE VALUES (null, 'Default', INBOX, false)
INSERT INTO NODE VALUES (null, 'GMail', INBOX, true)
INSERT INTO NODE VALUES (null, 'Work Outlook', INBOX, true)
INSERT INTO NODE VALUES (null, 'Weber Email', INBOX, true)
INSERT INTO NODE VALUES (null, 'Recurring Tasks', INBOX, true)
INSERT INTO NODE VALUES (null, 'Web Clips', INBOX, true)

INSERT INTO NODE VALUES (null, 'Home Triage', TRIAGE, true)
INSERT INTO NODE VALUES (null, 'Work Triage', TRIAGE, true)
INSERT INTO NODE VALUES (null, 'School Triage', TRIAGE, true)

INSERT INTO NODE VALUES (null, 'Programming References', REFERENCE, true)
INSERT INTO NODE VALUES (null, 'Career References', REFERENCE, true)
INSERT INTO NODE VALUES (null, 'Domestic References', REFERENCE, true)
INSERT INTO NODE VALUES (null, 'Work References', REFERENCE, true)
INSERT INTO NODE VALUES (null, 'Physical References', REFERENCE, true)
INSERT INTO NODE VALUES (null, 'Mental/Spiritual References', REFERENCE, true)

INSERT INTO NODE VALUES (null, 'Dormant Projects', PROJECTS, true)
INSERT INTO NODE VALUES (null, 'Incubative Projects', PROJECTS, true)
INSERT INTO NODE VALUES (null, 'Active Home Projects', PROJECTS, true)
INSERT INTO NODE VALUES (null, 'Active Work Projects', PROJECTS, true)
INSERT INTO NODE VALUES (null, 'Active School Projects', PROJECTS, true)

INSERT INTO NODE VALUES(null, 'Upcoming this Year', KANBAN, false)
INSERT INTO NODE VALUES(null, 'Upcoming this Month', KANBAN, true)
INSERT INTO NODE VALUES(null, 'Upcoming this Week', KANBAN, true)
INSERT INTO NODE VALUES(null, 'Upcoming Ubermorgen', KANBAN, true)
INSERT INTO NODE VALUES(null, 'Upcoming Tomorrow', KANBAN, true)
INSERT INTO NODE VALUES(null, 'Todays Backlog', KANBAN, true)

INSERT INTO NODE VALUES(null, 'Current Focus', KANBAN, true)
INSERT INTO NODE VALUES(null, 'Completed Today', KANBAN, true)
INSERT INTO NODE VALUES(null, 'Completed Yesterday', KANBAN, false)
INSERT INTO NODE VALUES(null, 'Completed this Week', KANBAN, false)



/* ACTIONABLES ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ */
CREATE TABLE ACTIONABLE(
    aa_id                   INTEGER                         PRIMARY KEY NOT NULL,
    aa_title                VARCHAR(50)                     NOT NULL,
    aa_parent_id            INTEGER                         NULL,
    aa_content              LONGTEXT CHARACTER SET UNICODE  NOT NULL,
    aa_duedate              DATETIME                        NULL,
    aa_suggested_duration   SMALLINT                        NULL,     
    aa_point_estimation     SMALLINT                        NULL
);
#INSERT INTO ACTIONABLE VALUES (aa_id, aa_title, aa_parent_id, aa_duedate, aa_suggested_duration, aa_point_estimation)
INSERT INTO ACTIONABLE VALUES (null, "Pay Rent", null, )