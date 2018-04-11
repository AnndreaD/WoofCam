<?php
// Initialize the session
session_start();

// If session variable is not set it will redirect to login page
if(!isset($_SESSION['username']) || empty($_SESSION['username'])){
  header("location: login.php");
  exit;
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Welcome</title>
    <link rel="stylesheet" href="styles.css">
    <style type="text/css">
    <img src="logo.jpg" width="380" height="125" />
    </style>
</head>
<body>
    <div class="page-header">
        <h1>Welcome<b><?php echo $_SESSION['username']; ?></b>, lets Woof and Stream!</h1>
    </div>

    <img src= "http://89.11.192.6:8081/" >
    <p><a href= "" class= "treatbtn"> Treat</a></p>
    <p><a href= "" class= "streambtn">Stream</a></p>



    <p><a href="logout.php" class="redbtn">Sign Out of Your Account</a></p>
</body>
</html>






