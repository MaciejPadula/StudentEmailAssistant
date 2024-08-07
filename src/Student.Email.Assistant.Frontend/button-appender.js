function tryAppendButton(parent, className, button) {
  const existingButton = parent.querySelector(`.${className}`);
  if (!existingButton) {
    parent.append(button);
  }
}