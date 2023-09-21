// function card() {
//     document.querySelector(".glass-card").classList.add("publish");
// }

// document.addEventListener('mouseup', function (e) {
//     var innerCard = document.querySelector('.inner-card')
//     if (!innerCard.contains(e.target)) {
//         document.querySelector(".glass-card").classList.remove("publish");
//     }
// });


function showDelete(element) {
    var courseId = element.dataset.courseId;
    var deleteLink = document.createElement('a');
    deleteLink.className = 'glass-delete'
    deleteLink.href = 'course/' + courseId + '/delete';
    deleteLink.innerHTML = 'Delete'
    var glassCardLinks = document.querySelector('.glass-card-links');
    glassCardLinks.appendChild(deleteLink)
    document.querySelector('.glass-card').style.display = 'block';
}

function hideDelete() {
    var deleteLink = document.querySelector('.glass-delete');
    deleteLink.remove()
    document.querySelector('.glass-card').style.display = 'none';
}