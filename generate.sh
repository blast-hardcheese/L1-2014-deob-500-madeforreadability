(echo '<html><head><link rel="stylesheet" href="swiss.css" type="text/css" /></head><body>'; markdown "$1"; echo '</body></html>') > "${1%%.md}.html"
