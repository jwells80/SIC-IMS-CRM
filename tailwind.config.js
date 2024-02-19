/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "../**/templates/**/*.html",
        "../**/static/**/*.js"
    ],
    theme: {
        extend: {},
    },
    plugins: [
        require("daisyui")
    ],
    daisyui: {
        themes: [
            {
                mytheme: {
                    "primary": "#009694",
                    "secondary": "#00c1ff",
                    "accent": "#ff0000",
                    "neutral": "#2f1e26",
                    "base-100": "#212730",
                    "info": "#008dff",
                    "success": "#00b180",
                    "warning": "#ffaa00",
                    "error": "#e51248",
                },
            },
        ],
    },
}