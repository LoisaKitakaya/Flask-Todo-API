const clearNotification = () => {
  const box = document.getElementById("flash-box");
  box.remove();
};

const secret = document.getElementById("secret");

const toggleFunc = () => {
  secret.classList.toggle("jwt-token");
};

const text = document.getElementById("token").innerHTML;

const copyContent = async () => {
  secret.select();

  try {
    await navigator.clipboard.writeText(text);
    alert("Token copied to clipboard");
  } catch (err) {
    alert("Failed to copy: ", err);
  }
};
