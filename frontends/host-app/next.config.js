const AUTH_APP_URL = 'http://localhost:3001';
const PRODUCTS_APP_URL = 'http://localhost:3002';

/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
  async rewrites() {
    return [
      {
        source: "/:path*", // www.3sixty.com
        destination: `/:path*`,
      },
      {
        source: "/auth", //// www.3sixty.com/auth
        destination: `${AUTH_APP_URL}/auth`,
      },
      {
        source: "/auth/:path*", // www.3sixty.com/auth/login | www.3sixty.com/auth/logout | www.3sixty.com/auth/register
        destination: `${AUTH_APP_URL}/auth/:path*`,
      },
      {
        source: "/products", //// www.3sixty.com/products
        destination: `${PRODUCTS_APP_URL}/products`,
      },
      {
        source: "/products/:path*", // www.3sixty.com/products/1 | www.3sixty.com/products/2 | www.3sixty.com/products/3/edit
        destination: `${PRODUCTS_APP_URL}/products/:path*`,
      },
    ];
  },
}

module.exports = nextConfig
