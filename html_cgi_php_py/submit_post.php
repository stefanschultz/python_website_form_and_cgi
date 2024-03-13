<?php
if (isset($_POST['forename']) && isset($_POST['surname'])) {
    $forename = htmlspecialchars($_POST['forename']);
    $surname = htmlspecialchars($_POST['surname']);
    echo "Hello, " . $forename . " " . $surname . "!";
} else {
    echo "Forename and surname are required.";
}
?>