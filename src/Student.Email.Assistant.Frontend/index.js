MutationObserver = window.MutationObserver || window.WebKitMutationObserver;

const link = document.createElement('link');
link.rel = 'stylesheet';
link.href = 'https://fonts.googleapis.com/icon?family=Material+Icons';
document.head.appendChild(link);

function addGenerateTitleButton(titleInput) {
  const generateTitleButtonClass = "generate-title";
  const btn = createIconButton(
    "psychology",
    generateTitleButtonClass,
    () => {}
  );
  btn.style.position = "absolute";
  btn.style.top = "0";
  btn.style.right = "0";

  tryAppendButton(titleInput, generateTitleButtonClass, btn);
}

function addImproveEmailButton(contentInput) {
  const improveContentButtonClass = "improve-content";
  const btn = createIconButton(
    "auto_fix_high",
    improveContentButtonClass,
    () => {}
  );
  btn.style.position = "absolute";
  btn.style.top = "0";
  btn.style.right = "0";

  tryAppendButton(contentInput, improveContentButtonClass, btn);
}

function processMailPopup(popup) {
  addGenerateTitleButton(popup.titleInput);
  addImproveEmailButton(popup.contentInput);
}

const observer = new MutationObserver(function (mutations, observer) {
  if (shouldRerender(mutations)) {
    const popups = getPopups();
    popups.forEach(processMailPopup);
  }
});

// define what element should be observed by the observer
// and what types of mutations trigger the callback
observer.observe(document, {
  subtree: true,
  attributes: true,
});
