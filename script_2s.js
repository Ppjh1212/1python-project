// let currentPage = 1;

// function changePage(delta) {
//   const coursesContainer = document.querySelector('.courses-container');
//   const totalPages = Math.ceil(coursesContainer.children.length / 5);

//   currentPage += delta;

//   if (currentPage > totalPages) {
//     currentPage = 1;
//   } else if (currentPage < 1) {
//     currentPage = totalPages;
//   }

//   document.querySelector('.page-number').textContent = currentPage;

//   const startIdx = (currentPage - 1) * 5;
//   const endIdx = startIdx + 5;

//   for (let i = 0; i < coursesContainer.children.length; i++) {
//     coursesContainer.children[i].style.display = i >= startIdx && i < endIdx ? 'block' : 'none';
//   }
// }

// // 초기 페이지 설정
// changePage(0);




let currentPage = 1;

async function fetchCourses() {
    const response = await fetch("/api/courses");
    const courses = await response.json();
    return courses;
}

async function updateCourses() {
    const coursesContainer = document.getElementById('courses-container');
    const courses = await fetchCourses();

    // 기존 코스를 비워주고 새로운 코스로 채워줍니다.
    coursesContainer.innerHTML = '';

    courses.forEach(course => {
        const courseElement = document.createElement('div');
        courseElement.className = 'course';

        const linkElement = document.createElement('a');
        linkElement.href = '#'; // 적절한 링크로 교체

        const imgElement = document.createElement('img');
        imgElement.src = `./이미지/${course.title}.png`; // 이미지 경로를 적절하게 변경
        imgElement.alt = 'Course Image';

        const detailsElement = document.createElement('div');
        detailsElement.className = 'course-details';

        const titleElement = document.createElement('div');
        titleElement.className = 'course-title';
        titleElement.textContent = course.title;

        const priceElement = document.createElement('div');
        priceElement.className = 'course-price';
        priceElement.textContent = course.price;

        // DOM에 요소들을 추가합니다.
        detailsElement.appendChild(titleElement);
        detailsElement.appendChild(priceElement);
        linkElement.appendChild(imgElement);
        linkElement.appendChild(detailsElement);
        courseElement.appendChild(linkElement);
        coursesContainer.appendChild(courseElement);
    });
}

// 초기 페이지 설정
updateCourses();