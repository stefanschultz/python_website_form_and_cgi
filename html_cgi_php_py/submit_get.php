<?php
if (isset($_GET['forename']) && isset($_GET['surname'])) {
    $forename = htmlspecialchars($_GET['forename']);
    $surname = htmlspecialchars($_GET['surname']);
    echo "Hello, " . $forename . " " . $surname . "!";
} else {
    echo "Forename and surname are required.";
}
?>