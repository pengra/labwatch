$(document).ready(function(){
  $('[data-toggle="tooltip"]').tooltip(); 
});

updateUrl = (tabId) => {
  window.history.pushState(null, tabId, '?tab=' + tabId);
}