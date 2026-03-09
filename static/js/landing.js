 const itemsArr = [
      { id: 1, url: 'https://images.unsplash.com/photo-1490481651871-ab68de25d43d?q=80&w=1200&auto=format', title: 'Streetwear', description: 'Discover the hottest streetwear from hundreds of brands. Fresh drops daily from Supreme, Off-White, and emerging designers.', tags: ['Hoodies', 'Sneakers', 'Graphic Tees', 'Limited Edition'] },
      { id: 2, url: 'https://images.unsplash.com/photo-1483985988355-763728e1935b?q=80&w=1200&auto=format', title: 'Designer Fashion', description: 'Luxury brands at your fingertips. Shop Gucci, Prada, Versace and more with same-day delivery in select areas.', tags: ['Luxury', 'High-End', 'Premium', 'Designer'] },
      { id: 3, url: 'https://images.unsplash.com/photo-1571945153237-4929e783af4a?q=80&w=1200&auto=format', title: 'Activewear', description: 'Gym ready, delivered fast. Nike, Adidas, Lululemon, and athletic gear from local sports stores near you.', tags: ['Fitness', 'Performance', 'Athleisure', 'Training'] },
      { id: 4, url: 'https://images.unsplash.com/photo-1434389677669-e08b4cac3105?q=80&w=1200&auto=format', title: 'Business Casual', description: 'Professional attire delivered on your schedule. From suits to dress shirts, look sharp without the shopping trip.', tags: ['Office', 'Professional', 'Formal', 'Business'] },
      { id: 5, url: 'https://images.unsplash.com/photo-1445205170230-053b83016050?q=80&w=1200&auto=format', title: 'Vintage & Thrift', description: 'Unique finds from local vintage shops and consignment stores. Sustainable fashion delivered to your door.', tags: ['Vintage', 'Thrift', 'Sustainable', 'One-of-a-Kind'] },
      { id: 6, url: 'https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?q=80&w=1200&auto=format', title: 'Accessories', description: 'Complete your look with bags, jewelry, watches, and more from boutiques and department stores.', tags: ['Bags', 'Jewelry', 'Watches', 'Sunglasses'] },
      { id: 7, url: 'https://images.unsplash.com/photo-1556906781-9a412961c28c?q=80&w=1200&auto=format', title: 'Footwear', description: 'Sneakers, boots, heels, and everything in between. Browse inventory from stores across your city.', tags: ['Sneakers', 'Boots', 'Heels', 'Sandals'] },
      { id: 8, url: 'https://images.unsplash.com/photo-1544441893-675973e31985?q=80&w=1200&auto=format', title: 'Summer Collection', description: 'Beach-ready styles, light fabrics, and warm weather essentials. Fresh summer picks from local retailers.', tags: ['Swimwear', 'Dresses', 'Shorts', 'Light Fabrics'] },
      { id: 9, url: 'https://images.unsplash.com/photo-1489987707025-afc232f7ea0f?q=80&w=1200&auto=format', title: 'Winter Wear', description: 'Stay warm with jackets, coats, and cold-weather gear from brands you love, delivered fast.', tags: ['Coats', 'Jackets', 'Sweaters', 'Warm'] },
      { id: 10, url: 'https://images.unsplash.com/photo-1441984904996-e0b6ba687e04?q=80&w=1200&auto=format', title: "Trending Now", description: "What's hot right now. Curated picks based on what's popular in your area this week.", tags: ['Popular', 'Trending', 'New Arrivals', 'Hot'] },
      { id: 11, url: 'https://images.unsplash.com/photo-1467043237213-65f2da53396f?q=80&w=1200&auto=format', title: 'Local Boutiques', description: 'Support local businesses. Unique pieces from independent stores and designers in your neighborhood.', tags: ['Local', 'Independent', 'Small Business', 'Unique'] },
    ];

    function loadVideoBackground() {
      const videoContainer = document.getElementById('videoBackground');
      const video = document.createElement('video');
      video.autoplay = true;
      video.muted = true;
      video.loop = true;
      video.playsInline = true;
      video.preload = 'metadata';

      const sourceEl = document.createElement('source');
      // ONLY CHANGE: Django static path
      sourceEl.src = "{% static 'video/fresh_fits.mp4' %}";
      sourceEl.type = 'video/mp4';
      video.appendChild(sourceEl);

      video.addEventListener('error', () => {
        videoContainer.style.background = 'linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #0f3460 100%)';
      });

      videoContainer.appendChild(video);
      video.play().catch(() => {});
    }

    function scrollToGallery() {
      document.getElementById('gallery-section').scrollIntoView({ behavior: 'smooth' });
    }

    // ✅ Visible parallax: translate + scale while hero is on screen
    function initHeroParallax() {
      const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
      if (reduceMotion) return;

      const hero = document.getElementById("hero");
      const bg = document.getElementById("videoBackground");
      const overlay = document.getElementById("videoOverlay");
      const content = document.getElementById("heroContent");

      if (!hero || !bg || !overlay || !content) return;

      let ticking = false;

      function clamp(n, min, max) { return Math.min(max, Math.max(min, n)); }

      function update() {
        const rect = hero.getBoundingClientRect();
        const heroH = rect.height || window.innerHeight;

        // progress: 0 when top of hero at top of viewport; 1 when hero fully scrolled past
        const scrolled = clamp((0 - rect.top) / heroH, 0, 1);

           // You can tweak these for stronger/weaker effect:
        const bgY = scrolled * -90;       // px
        const overlayY = scrolled * -45;  // px
        const contentY = scrolled * 18;   // px (opposite direction)

        const bgScale = 1 + scrolled * 0.08;       // subtle zoom
        const overlayScale = 1 + scrolled * 0.03;  // tiny zoom

        bg.style.transform = `translate3d(0, ${bgY}px, 0) scale(${bgScale})`;
        overlay.style.transform = `translate3d(0, ${overlayY}px, 0) scale(${overlayScale})`;
        content.style.transform = `translate3d(0, ${contentY}px, 0)`;

        ticking = false;
      }

      function onScroll() {
        if (ticking) return;
        ticking = true;
        requestAnimationFrame(update);
      }

      window.addEventListener("scroll", onScroll, { passive: true });
      window.addEventListener("resize", onScroll, { passive: true });
      update();
    }

    // Gallery
    let currentIndex = 5;
    const gallery = document.getElementById('gallery');
    const galleryWrapper = document.getElementById('galleryWrapper');
    const detailView = document.getElementById('detailView');
    const closeDetail = document.getElementById('closeDetail');
    const detailImage = document.getElementById('detailImage');
    const detailTitle = document.getElementById('detailTitle');
    const detailDescription = document.getElementById('detailDescription');
    const detailTags = document.getElementById('detailTags');

    function initGallery() {
      gallery.innerHTML = '';
      itemsArr.forEach((item, index) => {
        const galleryItem = document.createElement('div');
        galleryItem.className = 'gallery-item';
        if (index === currentIndex) galleryItem.classList.add('active');

        const img = document.createElement('img');
        img.src = item.url;
        img.alt = item.title;
        img.loading = 'lazy';
        img.draggable = false;
        galleryItem.appendChild(img);

        galleryItem.addEventListener('mouseenter', () => setActiveItem(index));
        galleryItem.addEventListener('click', () => openDetailView(index));

        gallery.appendChild(galleryItem);
      });

      enableGalleryDragScroll();
    }

    function setActiveItem(index) {
      currentIndex = index;
      document.querySelectorAll('.gallery-item').forEach((item, i) => {
        item.classList.toggle('active', i === index);
      });
    }

    function openDetailView(index) {
      const item = itemsArr[index];
      detailImage.src = item.url;
      detailImage.alt = item.title;
      detailTitle.textContent = item.title;
      detailDescription.textContent = item.description;

      detailTags.innerHTML = '';
      item.tags.forEach(tag => {
        const tagEl = document.createElement('span');
        tagEl.className = 'detail-tag';
        tagEl.textContent = tag;
        detailTags.appendChild(tagEl);
      });

      detailView.classList.add('active');
      document.body.style.overflow = 'hidden';
    }

    function closeDetailView() {
      detailView.classList.remove('active');
      document.body.style.overflow = '';
    }

    closeDetail.addEventListener('click', closeDetailView);
    detailView.addEventListener('click', (e) => { if (e.target === detailView) closeDetailView(); });
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && detailView.classList.contains('active')) closeDetailView(); });

    function enableGalleryDragScroll() {
      let isDown = false;
      let startX = 0;
      let scrollLeft = 0;

      const scroller = galleryWrapper;

      scroller.addEventListener('mousedown', (e) => {
        isDown = true;
        startX = e.pageX - scroller.offsetLeft;
        scrollLeft = scroller.scrollLeft;
      });
      scroller.addEventListener('mouseleave', () => isDown = false);
      scroller.addEventListener('mouseup', () => isDown = false);

      scroller.addEventListener('mousemove', (e) => {
        if (!isDown) return;
        e.preventDefault();
        const x = e.pageX - scroller.offsetLeft;
        const walk = (x - startX) * 2;
        scroller.scrollLeft = scrollLeft - walk;
      });

      scroller.addEventListener('touchstart', (e) => {
        isDown = true;
        startX = e.touches[0].pageX - scroller.offsetLeft;
        scrollLeft = scroller.scrollLeft;
      }, { passive: true });

      scroller.addEventListener('touchend', () => isDown = false);

      scroller.addEventListener('touchmove', (e) => {
        if (!isDown) return;
        const x = e.touches[0].pageX - scroller.offsetLeft;
        const walk = (x - startX) * 2;
        scroller.scrollLeft = scrollLeft - walk;
      }, { passive: true });
    }

    document.addEventListener('DOMContentLoaded', () => {
      loadVideoBackground();
      initGallery();
      initHeroParallax();
    });