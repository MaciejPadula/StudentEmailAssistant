function createIconButton(text, className, onClick) {
  const button = document.createElement("div");
  button.className = className;
  button.classList.add("assistant-icon-button");
  button.innerHTML = `
<span class="material-icons">
    ${text}
</span>
`;
  button.onclick = onClick;
  return button;
}
