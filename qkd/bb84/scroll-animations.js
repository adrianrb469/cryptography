// Scroll animations
document.addEventListener("DOMContentLoaded", function () {
  // Function to check if element is in viewport
  function isInViewport(element) {
    const rect = element.getBoundingClientRect();
    return (
      rect.top >= 0 &&
      rect.left >= 0 &&
      rect.bottom <=
        (window.innerHeight || document.documentElement.clientHeight) &&
      rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
  }

  // Function to check if element is partially in viewport
  function isPartiallyInViewport(element) {
    const rect = element.getBoundingClientRect();
    return (
      rect.top <
        (window.innerHeight || document.documentElement.clientHeight) &&
      rect.bottom >= 0
    );
  }

  // Get all elements that should animate
  const animateElements = document.querySelectorAll(".point, .step");

  // Function to handle scroll animations
  function handleScrollAnimations() {
    animateElements.forEach((element) => {
      if (
        isPartiallyInViewport(element) &&
        !element.classList.contains("animate")
      ) {
        // Add a small delay for staggered animation
        const delay =
          Array.from(element.parentNode.children).indexOf(element) * 200;
        setTimeout(() => {
          element.classList.add("animate");
        }, delay);
      }
    });
  }

  // Smooth scrolling for anchor links (if any)
  function smoothScroll() {
    const links = document.querySelectorAll('a[href^="#"]');
    links.forEach((link) => {
      link.addEventListener("click", function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute("href"));
        if (target) {
          target.scrollIntoView({
            behavior: "smooth",
            block: "start",
          });
        }
      });
    });
  }

  // Initialize
  handleScrollAnimations();
  smoothScroll();

  // Listen for scroll events
  let ticking = false;
  function onScroll() {
    if (!ticking) {
      requestAnimationFrame(() => {
        handleScrollAnimations();
        ticking = false;
      });
      ticking = true;
    }
  }

  window.addEventListener("scroll", onScroll);

  // Also trigger on resize
  window.addEventListener("resize", handleScrollAnimations);
});
