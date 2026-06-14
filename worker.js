export default {
  async fetch(request) {
    const url = new URL(request.url);

    // /tarot redirect to AI Tarot site
    if (url.pathname === '/tarot' || url.pathname === '/tarot/') {
      return Response.redirect('https://jbxgithub.github.io/ai-tarot/', 301);
    }

    // All other requests pass through
    return fetch(request);
  }
};