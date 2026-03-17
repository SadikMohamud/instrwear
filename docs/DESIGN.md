# Design

## Design Approach

InstrWear follows a bold, high-contrast neo-brutalist design direction adapted for a Django application. The design system was chosen to give the platform a strong visual identity, making it feel energetic, modern, and distinct from conventional e-commerce interfaces.

The implementation prioritises:

- strong visual hierarchy
- thick borders and hard shadows
- highly legible typography
- clear separation between interface sections
- responsive layouts across device sizes
- maintainable styling patterns that can scale with the application

---

## Design Goals

The design system was applied to achieve the following goals:

- create an instantly recognisable visual identity
- avoid generic marketplace styling
- give interactive components a tactile, physical feel
- improve visual consistency across templates
- support both shopper-facing and merchant-facing views with a unified system
- ensure accessibility through high contrast and clear structure

---

## Visual Direction

The project adopts a neo-brutalist interface style characterised by:

- heavy black borders
- hard-edged offset shadows
- strong blocks of colour
- bold typography
- sharp rectangular surfaces
- asymmetrical composition
- sticker-like layering and rotation
- fast, mechanical interaction feedback

This approach was selected to make the platform feel expressive and memorable while still remaining functional and readable.

---

## Design Tokens

### Colour Palette

The interface uses a high-contrast palette built around a paper-like neutral background and saturated accent colours.

- **Background:** `#FFFDF5`
- **Foreground / Borders / Shadows:** `#000000`
- **Accent:** `#FF6B6B`
- **Secondary:** `#FFD93D`
- **Muted:** `#C4B5FD`
- **White:** `#FFFFFF`

### Typography

The primary typeface used in the design system is **Space Grotesk**.

Typography principles:

- heavy font weights
- large, high-impact headings
- uppercase labels and buttons
- tight headline spacing
- highly legible body text

### Surfaces and Borders

- sharp corners by default
- thick black borders as a core visual rule
- hard offset shadows for depth
- minimal reliance on soft effects

### Motion

Interactions are designed to feel mechanical rather than soft.

Examples include:

- buttons pressing inward on click
- cards lifting on hover
- fast transition timings
- playful but direct visual feedback

---

## Layout Principles

The layout system follows a responsive, mobile-first structure and is built around:

- strong section separation
- asymmetrical composition where appropriate
- consistent container widths
- dense but controlled spacing
- deliberate use of overlap and layering in key areas
- structured visual rhythm through alternating surfaces and colour blocks

---

## Responsiveness

The design system was adapted to remain usable across desktop, tablet, and mobile breakpoints.

Responsive considerations include:

- stacked layouts on smaller screens
- scaled typography across breakpoints
- touch-friendly input and button sizing
- preserved contrast and border visibility on mobile devices
- consistent interaction patterns regardless of screen size

---

## Accessibility Considerations

Accessibility was considered throughout the design process.

Key measures include:

- high-contrast colour combinations
- clear component boundaries
- strong visual focus states
- readable font sizing
- semantic structure in templates
- support for keyboard navigation
- avoidance of low-contrast greys and overly subtle UI states

---

## Wireframes

Add your wireframes below once completed.

### Landing Page Wireframe
![Landing Page Wireframe](../assets/screenshots/wireframe-landing.png)

### Product Listing Wireframe
![Product Listing Wireframe](../assets/screenshots/wireframe-product-list.png)

### Checkout Wireframe
![Checkout Wireframe](../assets/screenshots/wireframe-checkout.png)

### Merchant Flow Wireframe
![Merchant Flow Wireframe](../assets/screenshots/wireframe-merchant-flow.png)

---

## Agile Design Process

The project was developed using an iterative workflow supported by Agile planning principles.

### Kanban Board
![Kanban Board](../assets/screenshots/kanban-board.png)

### User Stories
![User Stories](../assets/screenshots/user-stories.png)

These artefacts were used to plan functionality, prioritise tasks, and structure feature delivery throughout development.

---

## Design Attribution

The neo-brutalist design direction used in this project was informed by a prompt-based design system workflow inspired by:

`https://www.designprompts.dev/`

The original prompt was adapted and refined to suit the architecture, templating, and styling constraints of this Django-based application.

---

## Adapted Design Prompt Reference

The following prompt informed the visual direction of the project and was further tailored for integration into the Django codebase:

> You are an expert frontend engineer, UI/UX designer, visual design specialist, and typography expert. Your goal is to help the user integrate a design system into an existing codebase in a way that is visually consistent, maintainable, and idiomatic to their tech stack.
>
> Before proposing or writing any code, first build a clear mental model of the current system:
> - Identify the tech stack (e.g. React, Next.js, Vue, Tailwind, shadcn/ui, etc.).
> - Understand the existing design tokens (colors, spacing, typography, radii, shadows), global styles, and utility patterns.
> - Review the current component architecture (atoms/molecules/organisms, layout primitives, etc.) and naming conventions.
> - Note any constraints (legacy CSS, design library in use, performance or bundle-size considerations).
>
> Ask the user focused questions to understand the user's goals. Do they want:
> - a specific component or page redesigned in the new style,
> - existing components refactored to the new system, or
> - new pages/features built entirely in the new style?
>
> Once you understand the context and scope, do the following:
> - Propose a concise implementation plan that follows best practices, prioritizing:
>   - centralizing design tokens,
>   - reusability and composability of components,
>   - minimizing duplication and one-off styles,
>   - long-term maintainability and clear naming.
> - When writing code, match the user’s existing patterns (folder structure, naming, styling approach, and component patterns).
> - Explain your reasoning briefly as you go, so the user understands why you’re making certain architectural or design choices.
>
> Always aim to:
> - Preserve or improve accessibility.
> - Maintain visual consistency with the provided design system.
> - Leave the codebase in a cleaner, more coherent state than you found it.
> - Ensure layouts are responsive and usable across devices.
> - Make deliberate, creative design choices that express the design system’s personality instead of producing a generic UI.

### Neo-Brutalist Prompt Notes

The original design prompt was then extended with a neo-brutalist system covering:

- design philosophy
- colour tokens
- typography rules
- borders and shadows
- component behaviour
- layout principles
- motion
- responsive strategy
- accessibility expectations

For project documentation purposes, the full expanded internal prompt can be retained separately if needed, while this section documents the origin and adaptation of the design approach used in the final implementation.



## Prompt-Assisted Design Workflow

Parts of the visual direction, design system thinking, and implementation planning were developed using prompt-assisted workflows. These prompts were then refined and adapted to suit the Django codebase, existing project structure, and frontend requirements.

For the full prompt archive used during development, see [PROMPTS.md](PROMPTS.md).