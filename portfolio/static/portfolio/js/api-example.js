/**
 * Portfolio API Integration
 * Bu fayl Django backend bilan ishlash uchun misol kod
 */

// API Base URL - backend manzili
const API_BASE_URL = 'http://localhost:8000/api';

/**
 * API dan ma'lumot olish uchun yordamchi funksiya
 */
async function fetchAPI(endpoint) {
  try {
    const response = await fetch(`${API_BASE_URL}${endpoint}`);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error(`API Error (${endpoint}):`, error);
    throw error;
  }
}

/**
 * API ga ma'lumot yuborish uchun yordamchi funksiya
 */
async function postAPI(endpoint, data) {
  try {
    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data)
    });
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error(`API Error (${endpoint}):`, error);
    throw error;
  }
}

/**
 * Portfolio API Class
 */
class PortfolioAPI {
  /**
   * Profil ma'lumotlarini olish
   */
  static async getProfile() {
    return await fetchAPI('/profile/');
  }

  /**
   * Barcha xizmatlarni olish
   */
  static async getServices() {
    return await fetchAPI('/services/');
  }

  /**
   * Timeline ma'lumotlarini olish
   * @param {string} type - 'education' yoki 'experience' yoki null (hammasi)
   */
  static async getTimeline(type = null) {
    const endpoint = type ? `/timeline/?type=${type}` : '/timeline/';
    return await fetchAPI(endpoint);
  }

  /**
   * Barcha ko'nikmalarni olish
   */
  static async getSkills() {
    return await fetchAPI('/skills/');
  }

  /**
   * Loyihalar kategoriyalarini olish
   */
  static async getCategories() {
    return await fetchAPI('/categories/');
  }

  /**
   * Loyihalarni olish
   * @param {string} category - Kategoriya slug (optional)
   * @param {boolean} featured - Faqat featured loyihalar (optional)
   */
  static async getProjects(category = null, featured = null) {
    let endpoint = '/projects/';
    const params = [];
    if (category) params.push(`category=${category}`);
    if (featured) params.push('featured=true');
    if (params.length > 0) endpoint += '?' + params.join('&');
    return await fetchAPI(endpoint);
  }

  /**
   * Bitta loyiha ma'lumotini olish
   * @param {number} id - Loyiha ID
   */
  static async getProject(id) {
    return await fetchAPI(`/projects/${id}/`);
  }

  /**
   * Testimoniallarni olish
   */
  static async getTestimonials() {
    return await fetchAPI('/testimonials/');
  }

  /**
   * Mijozlar logotiplarini olish
   */
  static async getClients() {
    return await fetchAPI('/clients/');
  }

  /**
   * Blog postlarni olish
   * @param {number} page - Sahifa raqami (pagination)
   * @param {boolean} featured - Faqat featured postlar
   */
  static async getBlogPosts(page = 1, featured = null) {
    let endpoint = `/blog/?page=${page}`;
    if (featured) endpoint += '&featured=true';
    return await fetchAPI(endpoint);
  }

  /**
   * Bitta blog post olish
   * @param {string} slug - Blog post slug
   */
  static async getBlogPost(slug) {
    return await fetchAPI(`/blog/${slug}/`);
  }

  /**
   * Kontakt forma yuborish
   * @param {object} data - {full_name, email, message}
   */
  static async submitContact(data) {
    return await postAPI('/contact/', data);
  }
}

/**
 * Sahifa yuklanganda ma'lumotlarni olish
 *
 * MUHIM: Bu faylni index.html ga qo'shing:
 * <script src="./assets/js/api-example.js"></script>
 */
async function initializePortfolio() {
  try {
    // Loading holati
    console.log('Loading portfolio data...');

    // Barcha ma'lumotlarni parallel yuklash
    const [profile, services, timeline, skills, projects, testimonials, clients, blogPosts] =
      await Promise.all([
        PortfolioAPI.getProfile(),
        PortfolioAPI.getServices(),
        PortfolioAPI.getTimeline(),
        PortfolioAPI.getSkills(),
        PortfolioAPI.getProjects(),
        PortfolioAPI.getTestimonials(),
        PortfolioAPI.getClients(),
        PortfolioAPI.getBlogPosts()
      ]);

    // Ma'lumotlarni UI ga ko'rsatish
    console.log('Profile:', profile);
    console.log('Services:', services);
    console.log('Timeline:', timeline);
    console.log('Skills:', skills);
    console.log('Projects:', projects);
    console.log('Testimonials:', testimonials);
    console.log('Clients:', clients);
    console.log('Blog Posts:', blogPosts);

    // Shu yerda UI yangilash funksiyalarini chaqiring
    // Masalan:
    // updateProfileUI(profile);
    // updateServicesUI(services);
    // updateProjectsUI(projects);
    // va hokazo...

    console.log('Portfolio data loaded successfully!');
  } catch (error) {
    console.error('Error initializing portfolio:', error);
    // Xatolik haqida foydalanuvchiga xabar berish
    showError('Failed to load portfolio data. Please try again later.');
  }
}

/**
 * Xatolik ko'rsatish funksiyasi
 */
function showError(message) {
  // Bu yerda xatolik xabarini ko'rsatish logikasi
  console.error(message);
  // Masalan, sahifada xabar ko'rsatish:
  // const errorDiv = document.createElement('div');
  // errorDiv.className = 'error-message';
  // errorDiv.textContent = message;
  // document.body.prepend(errorDiv);
}

/**
 * Kontakt forma handler
 */
function setupContactForm() {
  const form = document.querySelector('form[data-form]');
  if (!form) return;

  form.addEventListener('submit', async function(e) {
    e.preventDefault();

    const formData = {
      full_name: this.querySelector('[name="fullname"]').value,
      email: this.querySelector('[name="email"]').value,
      message: this.querySelector('[name="message"]').value
    };

    try {
      const response = await PortfolioAPI.submitContact(formData);
      alert('Thank you! Your message has been sent successfully.');
      form.reset();
    } catch (error) {
      alert('Failed to send message. Please try again.');
    }
  });
}

/**
 * Loyihalar filterlash
 */
function setupProjectFilters() {
  const filterButtons = document.querySelectorAll('[data-filter-btn]');

  filterButtons.forEach(button => {
    button.addEventListener('click', async function() {
      const category = this.dataset.filterBtn;

      try {
        let projects;
        if (category === 'all') {
          projects = await PortfolioAPI.getProjects();
        } else {
          // Category slug ni backend ga yuborish
          // Masalan: "Web Design" -> "web-design"
          const categorySlug = category.toLowerCase().replace(/\s+/g, '-');
          projects = await PortfolioAPI.getProjects(categorySlug);
        }

        // Loyihalarni UI da ko'rsatish
        console.log('Filtered projects:', projects);
        // updateProjectsUI(projects);
      } catch (error) {
        console.error('Error filtering projects:', error);
      }
    });
  });
}

// Sahifa yuklanganda ishga tushirish
if (typeof document !== 'undefined') {
  document.addEventListener('DOMContentLoaded', function() {
    initializePortfolio();
    setupContactForm();
    setupProjectFilters();
  });
}

// Export qilish (agar module ishlatilsa)
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { PortfolioAPI, initializePortfolio };
}
