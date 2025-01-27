# Definitions for pef.py

# exploitable functions
exploitableFunctions = [
    "system(",
    "exec(",
    "popen(",
    "pcntl_exec(",
    "eval(",
    "arse_str(", # use arse_str(, because somehow, parse_str causes "IndexError: list index out of range" o_O
    "parse_url(",
    "preg_replace(",
    "create_function(",
    "include(",
    "require(",
    "passthru(",
    "shell_exec(",
    "popen(",
    "proc_open(",
    "pcntl_exec(",
    "extract(",
    "putenv(",
    "ini_set(",
    "mail(",
    "header(",
    "unserialize(",
    "assert(",
    "call_user_func(",
    "call_user_func_array(",
    "ereg_replace(",
    "eregi_replace(",
    "mb_ereg_replace(",
    "mb_eregi_replace(",
    "virtual",
    "readfile(",
    "file_get_contents(",
    "show_source(",
    "highlight_file(",
    "fopen(",
    "file(",
    "fpassthru(",
    "fsockopen(",
    "gzopen(",
    "gzread(",
    "gzfile(",
    "gzpassthru(",
    "readgzfile(",
    "mssql_query(",
    "odbc_exec(",
    "sqlsrv_query(",
    "PDO::query(",
    "move_uploaded_file(",
    "echo",
    "print(",
    "printf(",
    "ldap_search(",
    "header(",
    "sqlite_",
    "sqlite_query(",
    "pg_",
    "pg_query(",
    "mysql_",
    "mysql_query(",
    "mysqli::query(",
    "mysqli_",
    "mysqli_query(",
    "apache_setenv(",
    "dl(",
    "escapeshellarg(",
    "escapeshellcmd(",
    "extract(",
    "get_cfg_var(",
    "get_current_user(",
    "getcwd(",
    "getenv(",
    "ini_restore(",
    "ini_set(",
    "passthru(",
    "pcntl_exec(",
    "php_uname(",
    "phpinfo(",
    "popen(",
    "proc_open(",
    "putenv(",
    "symlink(",
    "syslog(",
    "curl_exec(",
    "__wakeup(",
    "__destruct(",
    "__sleep(",
    "filter_var(",
    "file_put_contents("
]

# only high severity functions, for quick scan of large codebase
# to find oversighted leading to RCE, LFI, Command Injections, SQLi etc.
critical = [
    "system(",
    "exec(",
    "popen(",
    "pcntl_exec(",
    "eval(",
    "passthru(",
    "shell_exec(",
    "extract(",
    "putenv(",
    "unserialize(",
    "readfile(",
    "file_get_contents(",
    "mysql_query(",
    "mssql_query(",
    "sqlite_query(",
    "pg_query(",
    "__wakeup(",
    "__destruct(",
    "__sleep(",
    "__call(",
    "__callStatic(",
    "file_put_contents("
]

# dangerous global(s)
globalVars = [
    "$_POST",
    "$_GET",
    "$_COOKIE",
    "$_REQUEST",
    "$_SERVER"
]

# dangerous patterns - LFI/RFI
fileInclude = [
    "include($_GET",
    "require($_GET",
    "include_once($_GET",
    "require_once($_GET",
    "include($_REQUEST",
    "require($_REQUEST",
    "include_once($_REQUEST",
    "require_once($_REQUEST"
]

# reflected properties which might leads to eg. XSS
reflectedProperties = [
    "$_SERVER[\"PHP_SELF\"]",
    "$_SERVER[\"SERVER_ADDR\"]",
    "$_SERVER[\"SERVER_NAME\"]",
    "$_SERVER[\"REMOTE_ADDR\"]",
    "$_SERVER[\"REMOTE_HOST\"]",
    "$_SERVER[\"REQUEST_URI\"]",
    "$_SERVER[\"HTTP_USER_AGENT\"]"
]

# other patterns
otherPatterns = [
    "SELECT.*FROM",
    "INSERT.*INTO",
    "UPDATE.*",
    "DELETE.*FROM"
]