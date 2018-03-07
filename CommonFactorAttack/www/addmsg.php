<?php
if (isset($_POST['user_id']) && isset($_POST['content'])) {
  $user_id = $_POST['user_id'];
  $content = $_POST['content'];

  if ($user_id != "" && $content != "") {
    $db = new PDO('sqlite:users.db');
  	$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
  	$sql = "INSERT INTO messages(user_id, content) VALUES(:user_id, :content)";
  	$stmt = $db->prepare($sql);
  	$stmt->execute(array("user_id" => $user_id, "content" => $content));  
  }
}

header("Location: /");
 ?>
