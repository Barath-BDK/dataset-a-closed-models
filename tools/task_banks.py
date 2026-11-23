"""Task sentences for the AI-written rows. Language neutral, no hint of a weakness or a fix. Each cell uses at least 40 different ones."""

VULN_TASKS = {
    "CWE-89": """Find a customer record by email address.
List a user's orders with a given status.
Search products whose name contains a keyword.
Check a username and password hash for a login.
Return the stock quantity for a product code.
Update the email address of a user profile.
Delete expired sessions older than a number of days.
Record an audit entry for an administrator action.
Report order totals grouped by a chosen category.
Return a page of articles sorted by a column chosen by the caller.
Search support tickets by keyword and priority.
List the employees of a department.
Find books by author name.
Count signups per day for a date range.
Fetch an invoice by its number.
Look up a city by postal code.
List the appointments of a doctor on a given day.
Set the stock quantity of a product after a delivery.
Find articles that carry a given tag.
Export the orders of a given month.
Find the members of a team by role.
Return the latest comments on a post.
Look up a coupon by its code.
Mark a notification as read for a user.
Find a vehicle by its registration number.
List reservations for a room between two dates.
Find all students enrolled in a course.
Look up the shipping address of an order.
Count the unread messages of a user.
Search a product catalogue with optional filters for price and brand.
Delete a user's saved bookmarks that match a title.
Insert a new product review.
List the most recent log entries of a service.
Find patients by surname.
Transfer a balance between two accounts inside a transaction.
Fetch the configuration value for a given key and environment.
List the files shared with a user.
Find events happening in a given city.
Update the status of a support ticket.
Return the top sellers for a given region.
Find all accounts created through an affiliate code.
Search a phone book by name prefix.
Remove a product from a wishlist.
Get the loyalty points of a customer.
List recent transactions for an account sorted by amount or date.""".split("\n"),
    "CWE-78": """Check whether a host answers a network ping.
Look up the DNS records of a host name.
Unpack an uploaded archive into a working folder.
Zip the contents of a folder into a named archive.
Resize an image to a requested size with an external tool.
Extract a thumbnail frame from a video file.
Show the commit history of a repository for one author.
Search a log file for lines containing a term.
Compress a log file after rotation.
Compute the checksum of a file.
Restart a named system service.
Report the disk usage of a folder.
Send a document to a named printer.
Download a web page with a command line client.
Read the expiry date of a certificate file.
Back up a directory to another location with a sync tool.
Check whether a port is open on a host.
Count the lines of a file with a standard tool.
Run a code formatter on a source file.
Run a linter on a submitted file and return its report.
Show the mount information of a device.
Convert a document to another format with a converter.
Query the status of a container by name.
Read the last lines of a log file.
Trace the network route to a host.
Show the owner and permissions of a file.
Look up the registration data of a domain.
Start a background job from a script name.
Rotate the logs of one application.
Mount a network share with given options.
Run a database backup tool for one schema.
Compare two files and show the differences.
Print the version of a tool chosen from a list.
Pack an installer from a folder with a packaging tool.
Scan an uploaded file with a command line scanner.
Convert an audio file to another bitrate.
Add a user to a group with the system tool.
Run a spell checker on a text file.
Sync a folder to a remote host over ssh.
Execute a report generator with a chosen template.
Stop a process by name.
Create a snapshot of a virtual machine by name.
Run a unit conversion script on a value.
Show the fingerprint of an ssh key file.
Query a package manager for the version of a package.""".split("\n"),
    "CWE-22": """Return the text of an uploaded file.
Delete a user's attachment.
Rename a document inside the storage folder.
Save a note under a given name.
List the files in a sub folder of the storage area.
Serve a static asset such as an image or stylesheet.
Extract the entries of an uploaded archive into a folder.
Copy a template file into a user's workspace.
Report the size of a stored file.
Let a user download a generated report by name.
Store a user's avatar image.
Load a configuration file for a named profile.
Append a line to a user's activity log.
Load the translation file for a locale.
Return a preview of a stored image.
Read a log file of a named service.
Move a processed file to an archive folder.
Create a backup copy of a document.
Read the lines of a CSV import file.
Return the modification time of a stored file.
Check whether a named file exists in the storage area.
Open a certificate file by name.
Read an email template by name.
Write an exported spreadsheet under a requested name.
Return the contents of a help page file.
Delete temporary files that match a name.
Read a plugin manifest from a plugin folder.
Read a user's saved draft.
Hash the contents of a stored file.
Read a font file requested by a stylesheet.
Create a thumbnail file next to the original image.
Serve a PDF from the document library.
Read a language pack for a game.
Write a crash report file under a given id.
Restore a document from a version folder.
Truncate a log file chosen by name.
Read the first line of a stored file.
Fetch a user's uploaded resume.
Unzip a theme package into the themes folder.
Read a data file for a selected report.
Write a user's settings file.
Count the lines of a stored text file.
Open a video file for streaming.
Return the contents of a shared snippet file.
Remove an old export file.""".split("\n"),
    "CWE-338": """Create a session identifier for a signed-in user.
Generate a password reset token to email to a user.
Issue an API key for a new client.
Create a one-time code for two-factor sign in.
Generate a temporary password for a new account.
Create an invite code for a team.
Generate a CSRF token for a form.
Create a salt for hashing a password.
Generate a nonce for a signed request.
Create a key for a private download link.
Generate a pairing code for a device.
Create a verification code for a phone number.
Issue an email confirmation token.
Generate a one-time login link token.
Create a share link secret for a document.
Generate an access token for a mobile app.
Create an encryption key for a local vault.
Generate an initialization vector for encrypting a file.
Create a webhook signing secret.
Issue a gift card code with a check value.
Generate a PIN for a card activation.
Create a list of recovery codes for an account.
Generate a bearer token for a service account.
Create an unguessable id for a private upload.
Issue a ticket secret for a QR code.
Create a cookie value for a remember-me login.
Generate a shared secret for a time-based one-time password setup.
Create a challenge string for a login handshake.
Issue an invitation link token.
Pick the words of a recovery phrase for a wallet.
Create a password for a guest Wi-Fi voucher.
Generate a session key for an encrypted chat.
Create a deletion confirmation token.
Generate a license key for a software installation.
Issue a device registration token.
Create an OAuth state value for a login redirect.
Generate a booking confirmation code.
Issue a temporary access code for a visitor badge.
Create a private link token for a quiz.
Generate an unlock code for a smart lock.
Create a token for confirming a newsletter subscription.
Generate a one-time voucher for a refund.
Issue a short-lived upload key.
Create a nonce for a content security policy header.
Generate a secret for a shared team calendar link.""".split("\n"),
}

# CWE-338 hard negatives that use ordinary random for something harmless: pattern tag -> tasks
PLAIN_RANDOM_TASKS = {
    "ordinary_random_simulation": ["Simulate customer arrivals at a shop with random gaps between them.", "Estimate pi with a Monte Carlo simulation."],
    "ordinary_random_shuffling": ["Shuffle a playlist before playing it.", "Deal a shuffled deck of cards to four players."],
    "ordinary_random_sampling": ["Pick a random sample of users for a satisfaction survey.", "Choose which products to feature on the home page."],
    "ordinary_random_retry_jitter": ["Compute a retry delay with random jitter so clients do not retry together.", "Choose a polling interval spread between workers."],
    "ordinary_random_games": ["Roll dice for a board game.", "Pick a random spawn position for an enemy in a game."],
    "ordinary_random_test_data": ["Generate random names for test fixtures.", "Create random order amounts for a demo database."],
    "fixed_seed_reproducible": ["Draw the same sample every run for a reproducible experiment.", "Generate reproducible synthetic data for a unit test."],
}

NO_CODE_TASKS = {
    "CWE-89": """Format an order total with tax and currency.
Check the shape of an email address.
Parse a CSV line into fields.
Compute the average rating from a list.
Paginate a list in memory.
Build a display name from first and last name.
Group a list of records by a key.
Compute an age from a birth date.
Convert a status code into a label.
Merge two lists without duplicates.
Shorten a long description for a list view.
Compute a discount tier from an amount.""".split("\n"),
    "CWE-78": """Format a duration in seconds as hours and minutes.
Read the average time out of a ping summary text.
Check the shape of a host name string.
Turn a byte count into a short size label.
Count the non-empty lines of a text.
Build the text of a report header.
Compute a percentage of a total.
Pick the larger of two version strings.
Escape a string for display in an HTML page.
Convert Celsius to Fahrenheit.
Join a list of words into a title.
Check that a port number is in range.""".split("\n"),
    "CWE-22": """Get the extension of a file name given as text.
Normalize repeated slashes in a path string.
Compute a human readable size label.
Build a numbered report name from a prefix.
Check that a file name uses only plain characters.
Split a path string into its parts.
Return the parent part of a path string.
Count the segments of a path string.
Compare two version strings.
Format a timestamp for a file listing.
Pick an icon name from a file extension.
Shorten a long name with an ellipsis.""".split("\n"),
    "CWE-338": """Mask a token for display in a log line.
Group a token into blocks of four characters.
Compute the entropy of a value from its length and alphabet size.
Check that a token has the expected length and characters.
Compute the time left before a token expires.
Compare the lengths of two tokens.
Convert a token to uppercase for display.
Estimate password strength from its length.
Format a recovery code list for printing.
Split a token into its prefix and body.
Check that a code has only digits.
Compute the check digit of a number.""".split("\n"),
}
