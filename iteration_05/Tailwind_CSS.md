# Tailwind CSS Quick Reference for Flask Templates

## Adding Tailwind CSS to Your Base Template

To use Tailwind in your Flask app, add this `<script>` in the `<head>` of your **base.html**:

```html
<head>
    <title>{% block title %}My Page{% endblock %}</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
</head>
```


This guide lists useful Tailwind CSS utility classes organized by category.  
Each section explains **when** styles depend on a **parent container** — a crucial idea for layouts using `flex` and `grid`.

---

## Layout and Display

| Class | Description | Parent Dependency |
|-------|--------------|------------------|
| `flex` | Turns an element into a flex **container** | ✅ Affects all children |
| `grid` | Turns an element into a grid **container** | ✅ Affects all children |

### Example
```html
<div class="flex justify-center">
  <div class="p-4 bg-blue-200">Child 1</div>
  <div class="p-4 bg-blue-400">Child 2</div>
</div>
```
**Note:** The parent `.flex` defines the flex context — children respond to alignment and spacing from the parent.

---

## Spacing (Margin & Padding)

| Class | Description | Parent Dependency |
|-------|--------------|------------------|
| `m-4`, `mx-2`, `my-6` | Margin (outside spacing) | ❌ No |
| `p-4`, `px-2`, `py-6` | Padding (inside spacing) | ❌ No |
| `space-x-4`, `space-y-2` | Adds space **between flex/grid children** | ✅ Only works when parent is `flex` or `grid` |

### Example
```html
<div class="flex space-x-4">
  <div class="p-2 bg-green-300">Item 1</div>
  <div class="p-2 bg-green-500">Item 2</div>
</div>
```

---

## Flexbox Controls (Children of a Flex Container)

| Class | Description | Parent Dependency |
|-------|--------------|------------------|
| `justify-center`, `justify-between`, `justify-around` | Align children **horizontally** | ✅ Requires parent `.flex` |
| `items-center`, `items-start`, `items-end` | Align children **vertically** | ✅ Requires parent `.flex` |
| `flex-col`, `flex-row` | Direction of flex items | ✅ Requires parent `.flex` |
| `gap-4` | Adds spacing between items | ✅ Works best with `flex` or `grid` |

### Example
```html
<div class="flex flex-col items-center gap-2">
  <div class="bg-gray-200 p-2 w-1/2">Box A</div>
  <div class="bg-gray-300 p-2 w-1/2">Box B</div>
</div>
```

---

## Grid Layout

| Class | Description | Parent Dependency |
|-------|--------------|------------------|
| `grid-cols-2`, `grid-cols-3`, `grid-cols-4` | Number of columns | ✅ Requires parent `.grid` |
| `gap-4` | Space between grid cells | ✅ Works with `.grid` |
| `col-span-2` | Child spans multiple columns | ✅ Works only inside `.grid` |

### Example
```html
<div class="grid grid-cols-3 gap-4">
  <div class="bg-blue-200">1</div>
  <div class="bg-blue-300 col-span-2">2 (spans two columns)</div>
</div>
```

---

## Colors and Backgrounds

| Class | Description | Parent Dependency |
|-------|--------------|------------------|
| `bg-blue-500`, `bg-red-300` | Background colors | ❌ No |
| `text-white`, `text-gray-700` | Text colors | ❌ No |
| `hover:bg-blue-700` | Background color on hover | ❌ No |
| `opacity-50` | Make element semi-transparent | ❌ No |

---

## Typography

| Class | Description | Parent Dependency |
|-------|--------------|------------------|
| `text-sm`, `text-lg`, `text-2xl` | Font size | ❌ No |
| `font-bold`, `font-semibold`, `font-light` | Font weight | ❌ No |
| `text-center`, `text-left`, `text-right` | Text alignment | ❌ No |
| `leading-tight`, `tracking-wide` | Line height & letter spacing | ❌ No |

---

## Sizing and Borders

| Class | Description | Parent Dependency |
|-------|--------------|------------------|
| `w-1/2`, `w-full`, `h-32` | Width and height | ❌ No |
| `rounded`, `rounded-lg`, `rounded-full` | Border radius | ❌ No |
| `border`, `border-2`, `border-gray-400` | Adds border | ❌ No |
| `shadow`, `shadow-lg` | Drop shadow | ❌ No |

---

## Positioning

| Class | Description | Parent Dependency |
|-------|--------------|------------------|
| `relative`, `absolute`, `fixed` | Position modes | ✅ Sometimes (depends on parent if child uses `absolute`) |
| `top-0`, `bottom-4`, `left-1/2` | Position offsets | ✅ Parent must be `relative` if using child `absolute` |
| `z-10`, `z-50` | Stack order | ❌ No |

### Example
```html
<div class="relative">
  <img src="{{ url_for('static', filename='images/engagement_photo.jpg') }}" class="w-40 rounded-lg">
  <span class="absolute bottom-0 bg-black text-white text-sm p-1">Caption</span>
</div>
```

---

## Common Combos for Flask Templates

| Purpose | Example Classes | Parent Dependency |
|----------|-----------------|------------------|
| Center content on page | `flex justify-center items-center h-screen` | ✅ Yes |
| Simple card box | `p-4 bg-white shadow rounded` | ❌ No |
| Responsive image | `max-w-full h-auto rounded-lg` | ❌ No |
| Navbar | `flex justify-between items-center p-4 bg-gray-800 text-white` | ✅ Yes |

---

### Tip:
When debugging Tailwind layouts, **inspect the parent**.  
If `justify-*`, `items-*`, or `space-*` don’t work, check if the parent has `flex` or `grid` applied!

---

## Class Practice Challenge

Try adding Tailwind classes to your Flask pages:
1. Center your profile picture.
2. Create a “card” for your About section.
3. Use a grid layout for your contact links (email, GitHub, etc.).
4. Experiment with colors and hover effects.

---