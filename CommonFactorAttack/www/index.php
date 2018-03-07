<?php
  $db = new PDO('sqlite:users.db');
	$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
	$sql = "SELECT name, n, e, id FROM users";
	$stmt = $db->prepare($sql);
	$stmt->execute();
  $users = $stmt->fetchAll(PDO::FETCH_ASSOC);
 ?>
<!DOCTYPE html>
<html>
<head>
<title>RSA Workshop</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="w3.css">
<style>
body {
  background-color: grey;
}
</style>
</head>

<body>
<br /> <hr />

<div class="w3-content">
  <?php $i = 0;
  foreach ($users as $user) {

    if ($i % 4 == 0) {
      if ($i > 0) { ?>
      </div>
    <?php }?>
        <div class="w3-row">
    <?php } ?>

      <div class="w3-quarter">
        <div class="w3-card w3-dark-grey w3-margin w3-padding">
          <h3 class="w3-container w3-light-grey"><?=$user["name"]?></h3>
          <hr />
          <p>n: <?=$user["n"]?></p>
          <p>e: <?=$user["e"]?></p>
          <hr />
          <p>messages:</p>
          <ul class="w3-ul" style="height: 10em; overflow-y: scroll;">
          <?php
          $sql = "SELECT content FROM messages WHERE user_id = :id";
          $stmt = $db->prepare($sql);
          $stmt->execute(array(":id" => $user["id"]));
          $msgs = $stmt->fetchAll(PDO::FETCH_ASSOC);
          foreach ($msgs as $msg){
            echo "<li>" . $msg["content"] . "</li>";
          }
           ?>
          </ul>
          <hr />
          <form action="addmsg.php" method="post" class="w3-container">
              <input type="hidden" name="user_id" value='<?=$user["id"]?>' />
              <p><input type="text" name="content" placeholder="New message" class="w3-input w3-sand" /></p>
              <p><button type="submit" class="w3-btn w3-blue">Send msg</button></p>
          </form>
        </div>
      </div>

  <?php
  $i = $i + 1;
  }
  if ($i % 4 == 0) { echo "</div>"; }
   ?>
   <div class="w3-quarter">
     <div class="w3-card w3-margin w3-dark-grey">
       <form action="adduser.php" method="post" class="w3-container">
           <p><input type="text" name="name" placeholder="Name" class="w3-input w3-sand" /></p>
           <p><input type="text" name="n" placeholder="n" class="w3-input w3-sand" /></p>
           <p><input type="text" name="e" placeholder="e" class="w3-input w3-sand" /></p>
           <p><button type="submit" class="w3-btn w3-blue">Submit user</button></p>
       </form>
     </div>
   </div>
   <?php if ($i % 4 != 0) { echo "</div>"; } ?>
</div>

</body>
</html>
