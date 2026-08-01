import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import path from "path";

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
  server: {
    proxy: {
      "/auth": {
        target: "http://127.0.0.1:8000",
        changeOrigin: true,
      },
      "/users": {
        target: "http://127.0.0.1:8000",
        changeOrigin: true,
      },
      "/projects": {
        target: "http://127.0.0.1:8000",
        changeOrigin: true,
      },
      "/analysis": {
        target: "http://127.0.0.1:8000",
        changeOrigin: true,
      },
      "/assistant": {
        target: "http://127.0.0.1:8000",
        changeOrigin: true,
      },
    },
  },
});
