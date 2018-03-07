<?php
if (isset($_POST['name']) && isset($_POST['n']) && isset($_POST['e'])) {
  $name = $_POST['name'];
  $n = $_POST['n'];
  $e = $_POST['e'];

  if ($name != "" && $n != "" && $e != "") {
    $db = new PDO('sqlite:users.db');
  	$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
  	$sql = "INSERT INTO users(name, n, e) VALUES(:name, :n, :e)";
  	$stmt = $db->prepare($sql);
  	$stmt->execute(array("name" => $name, "n" => $n, "e" => $e));
  }
}

header("Location: /");
 ?>
