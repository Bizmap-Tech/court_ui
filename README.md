# Court UI Theme for Frappe v15

A modern, responsive UI theme specifically designed for Court Management Systems built on Frappe/ERPNext v15.

## Features

- Modern and clean interface
- Responsive design for all screen sizes
- Court-specific components and styling
- Optimized for Frappe v15
- Modular CSS architecture
- Custom components for court management
- Enhanced form and list views
- Specialized court calendar styling
- Status indicators for cases
- Judge and hearing management UI components

## Installation

1. Go to your bench directory:
```bash
cd frappe-bench
```

2. Get the app from GitHub:
```bash
bench get-app court_ui https://github.com/your-repo/court_ui
```

3. Install the app on your site:
```bash
bench --site your-site.com install-app court_ui
```

4. Build assets and restart:
```bash
bench build
bench restart
```

## Structure

The theme is organized into modular components:
- Base styles (variables, typography)
- Component-specific styles (forms, buttons, cards)
- Court-specific components
- Responsive design utilities
- Print styles

## Customization

You can customize the theme by modifying the CSS variables in `variables.css`. The modular structure makes it easy to modify specific components without affecting others.

## License

MIT