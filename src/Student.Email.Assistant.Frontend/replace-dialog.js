function openDialog(input) {
  const confirmed = confirm(input);

  return {  
    ok: confirmed,
    result: input
  }
}