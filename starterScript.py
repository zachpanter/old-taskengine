# IMPORTS
import hashlib
import binascii
import evernote.edam.userstore.constants as UserStoreConstants
import evernote.edam.type.ttypes as Types
import evernote.edam.limits.constants as Limits
import evernote.edam.notestore.ttypes as NoteStore
from evernote.api.client import EvernoteClient

# SET CONSTANTS
auth_token = "S=s1:U=91e89:E=1596cacfe43:C=15214fbcf68:P=1cd:A=en-devtoken:V=2:H=7e5994500c190be210d9273e0455dd3e"
backlogNotebookGUID = '67d020d0-e7fc-4eb4-acbf-63764f0124c8'
workingNotebookGUID = 'c26f3574-29bb-4a45-b799-64c972e3160b'
doneNotebookGUID = '57002a05-8b7f-4e71-adbe-7d6bb668efaf'

# GET CLIENT OBJECT
client = EvernoteClient(token=auth_token, sandbox=True)

# GET USER STORE OBJECT
user_store = client.get_user_store()

# GET NOTE STORE OBJECT
note_store = client.get_note_store()

# PREPARE FILTER OBJECT
generalFilter = NoteStore.NoteFilter()

# PREPARE ARGUMENTS FOR findNotesMetadata
i32offset = 0
resultSpec = NoteStore.NotesMetadataResultSpec()
resultSpec.includeTitle = 'TRUE'

# CHECK VERSION
version_ok = user_store.checkVersion("Evernote EDAMTest (Python)", UserStoreConstants.EDAM_VERSION_MAJOR, UserStoreConstants.EDAM_VERSION_MINOR)
if not version_ok:
    exit(1)

# MAIN PROGRAM LOOP
while True:
	print("Backlog\n")

	backlogNoteBook = note_store.getNotebook(auth_token, backlogNotebookGUID)
	backlogFilter = generalFilter
	backlogFilter.notebookGuid = backlogNotebookGUID
	backlogNotesMetadataList = note_store.findNotesMetadata(auth_token, backlogFilter, i32offset, Limits.EDAM_USER_NOTES_MAX, resultSpec) # NOT ITERABLE?!?!?!?
	for note in backlogNotesMetadataList:
		print(note.title)
		for tag in note.tagNames:
			print(tag)

	print("In Process\n")
	print("Done\n")
	print("\n")        
	
	try:
		x = int(raw_input("Press 3 to exit."))
	except:
		print("Invalid entry")
		continue
	
	if (int(x) == 3):
		exit(0)
	else:
		continue




def create_note()
	"""
	PURPOSE:
	PARAMETERS:
	RETURNS:
	"""

	# To create a new note, simply create a new Note object and fill in
	# attributes such as the note's title.
	note = Types.Note()
	note.title = "Test note 2 from EDAMTest.py"

	# To include an attachment such as an image in a note, first create a Resource
	# for the attachment. At a minimum, the Resource contains the binary attachment
	# data, an MD5 hash of the binary data, and the attachment MIME type.
	# It can also include attributes such as filename and location.
	image = open('enlogo.png', 'rb').read()
	md5 = hashlib.md5()
	md5.update(image)
	hash = md5.digest()

	data = Types.Data()
	data.size = len(image)
	data.bodyHash = hash
	data.body = image

	resource = Types.Resource()
	resource.mime = 'image/png'
	resource.data = data

	# Now, add the new Resource to the note's list of resources
	note.resources = [resource]

	# To display the Resource as part of the note's content, include an <en-media>
	# tag in the note's ENML content. The en-media tag identifies the corresponding
	# Resource using the MD5 hash.
	hash_hex = binascii.hexlify(hash)

	# The content of an Evernote note is represented using Evernote Markup Language
	# (ENML). The full ENML specification can be found in the Evernote API Overview
	# at http://dev.evernote.com/documentation/cloud/chapters/ENML.php
	note.content = '<?xml version="1.0" encoding="UTF-8"?>'
	note.content += '<!DOCTYPE en-note SYSTEM ' \
		'"http://xml.evernote.com/pub/enml2.dtd">'
	note.content += '<en-note>Here is the Evernote logo:<br/>'
	note.content += '<en-media type="image/png" hash="' + hash_hex + '"/>'
	note.content += '</en-note>'

	# Finally, send the new note to Evernote using the createNote method
	# The new Note object that is returned will contain server-generated
	# attributes such as the new note's unique GUID.
	created_note = note_store.createNote(note)

	print "Successfully created a new note with GUID: ", created_note.guid
