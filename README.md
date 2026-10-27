# Your Name. - UIX & Animated Background Edition.
Home Assistant theme inspired by Makoto Shinkai's 2016 film 君の名は。

Two modern dark variants, both built around frosted glass cards, a blurred background, and a shared amber accent that ties them together.

**Kataware-doki** — named after the split-twilight moment in the film. Deep indigo backgrounds, lavender as the primary colour, comet amber for active states. Warm and atmospheric.

**Tiamat** — named after the comet itself. Same structure, but the lavender is replaced with electric blue against a deep navy sky. Colder, more precise, still unmistakably the same world.

The older **Your Name. (UIX)** theme is retained separately in `themes/yourname_uix_original.yaml`; it is not merged into or rewritten as one of the modern variants.

---

WARNING! UIX custom add-in is strongly recommended!

* [Prerequisite](#prerequisite)
* [HACS installation](#hacs_installation)
* [Manual installation](#manual_installation)
* [Activate transparent Sidebar and animated background support](#activate_transparent_sidebar)
* [Activate animated Backgrounds](#activate_animations)
* [Enable the theme](#enable_the_theme)
* [Fonts](#fonts)
* [Bug](#bug)
* [Screenshots](#screenshots)

### <a name="prerequisite"></a>Prerequisite
Check if **configuration.yaml** allows themes loading from themes folder:

<pre>
frontend:
  themes: !include_dir_merge_named themes
</pre>

Check if the **themes** folder exists in **config** folder.   

Create it when none exists yet.

### <a name="hacs_installation"></a>HACS installation
1. Add `https://github.com/dreimer1986/yourname_uix` as a custom repository of type **Theme** if it is not already listed in HACS/Marketplace.
2. Download **Your Name. - UIX & Animated Background Edition**. Keep both YAML files from `themes/`: `yourname_uix.yaml` provides Kataware-doki and Tiamat; `yourname_uix_original.yaml` preserves the older theme separately. Current HACS installations copy both files.
3. Reload themes with the `frontend.reload_themes` action, or restart Home Assistant.
4. Install the supplemental static files below. Theme installation does not copy the repository's `www/` files into Home Assistant's `www/` directory.

### Supplemental weather icons and background

Download `yourname_uix-assets.zip` from the [latest release](https://github.com/dreimer1986/yourname_uix/releases/latest). Merge its `www/` directory into your Home Assistant **configuration directory** (usually `/config`), preserving existing unrelated files. Before the first release with this asset is published, copy the repository's `www/icons/` and `www/backgrounds/` directories manually.

Expected locations:

```text
/config/www/icons/sunny.svg
/config/www/icons/exceptional.svg
/config/www/backgrounds/yourname.jpg
```

The theme references `/local/icons/<weather-state>.svg`. All 15 referenced filenames are supplied; `exceptional.svg` is a static warning symbol, the other 14 are the restored weather artwork. The original theme currently uses a transparent background; its optional `/local/backgrounds/yourname.jpg` image is included for users who enable it themselves.

HACS manages the theme YAMLs; these supplemental files require the same copy/merge step when their release assets change. The original theme file and all its existing paths remain unchanged. UIX, fonts, and the background/glass plugin are separate dependencies, not installed by the theme package.

### <a name="manual_installation"></a>Manual installation

1. Create `/config/themes/yourname_uix/`.
2. Copy **both** files from `themes/` into it.
3. Copy the supplemental `www/` files as described above.
4. Reload themes or restart Home Assistant.

### <a name="activate_transparent_sidebar"></a>Activate transparent Sidebar and animated Background support

Install [Animated Backgrounds & Liquid Glass](https://github.com/dreimer1986/ha_animated_backgrounds#install) separately through HACS as a **Dashboard** repository. It bundles both the background engine and the glass module. Install UIX separately if you use the theme's UIX rules.

Merge the following into your existing configuration (do not create a second `frontend` section):

```yaml
frontend:
  themes: !include_dir_merge_named themes
  extra_module_url:
    - /hacsfiles/ha_animated_backgrounds/ha_animated_backgrounds.js
```

HACS normally registers the dashboard resource automatically. Restart Home Assistant after changing the global configuration and refresh the browser. Remove old `/local/styles.js?...` and `/local/ha-liquid-glass.js?...` entries from both global modules and dashboard resources when migrating. No separate `videoBackground.css` is needed.

### <a name="activate_animations"></a>Activate animated Backgrounds

Videos are not included. Place your own MP4/WebM files in `/config/www/animated_backgrounds/` and configure them in `/config/www/animated_backgrounds/config.json`:

```json
{
  "settings": {"weatherControl": false},
  "videoFiles": {"random": ["my-background.mp4", "evening.webm"]}
}
```

Existing Home Assistant helpers override matching JSON settings. See the [complete configuration reference](https://github.com/dreimer1986/ha_animated_backgrounds#config) for weather entities, helper names, page-specific videos, and video paths. These personal files are outside the HACS-managed plugin folder and survive plugin updates. Refresh the page after editing JSON; do not edit the installed JavaScript.

### <a name="enable_the_theme"></a>Enable the theme
- Open your **Profile** in Home Assistant and select **Your Name. - Kataware-doki (UIX)**, **Your Name. - Tiamat (UIX)**, or the older **Your Name. (UIX)**.

## <a name="fonts"></a>Fonts
The two themes use different fonts to match their mood. **Kataware-doki** uses Plus Jakarta Sans (warm, humanist) and **Tiamat** uses Sora (precise, quietly technical). Both fall back to system fonts if nothing is loaded.

To actually render them, add the following URL as a Lovelace resource:

**Settings → Dashboards → three-dot menu → Resources → Add Resource**

```
https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;1,400&family=Figtree:ital,wght@0,300;0,400;0,500;1,400&family=Sora:wght@300;400;500;600&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,400&display=swap
```

Set the resource type to **Stylesheet**. No restart needed. Hard-refresh your browser after (`Ctrl+Shift+R` / `Cmd+Shift+R`) if the font doesn't appear immediately.

> This requires your Home Assistant instance to have internet access. If you run fully offline the themes fall back to your system font automatically.

### <a name="bug"></a>Bug (?)
- Transparency can be a problem with some custom cards. Sometimes one of these added to the card in RAW Editor can fix things:
  - For Original 
  ```
      styles: |
      ha-card {
        --ha-card-background: rgba(0, 0, 0, 0.5) !important;
      }
  ```
  ```
     uix:
     style: |
       ha-card {
         --ha-card-background: rgba(0, 0, 0, 0.5) !important;
       }
  ```
  
  - For Kataware-doki
  ```
      styles: |
      ha-card {
        --ha-card-background: rgba(16, 12, 42, 0.50) !important;
      }
  ```
  ```
     uix:
     style: |
       ha-card {
         --ha-card-background: rgba(16, 12, 42, 0.50) !important;
       }
  ```
  
  - For Tiamat
  ```
      styles: |
      ha-card {
        --ha-card-background: rgba(8, 20, 44, 0.52) !important;
      }
  ```
  ```
     uix:
     style: |
       ha-card {
         --ha-card-background: rgba(8, 20, 44, 0.52) !important;
       }
  ```

- Install/update the background and glass engine through its separate Dashboard repository. The [background documentation](https://github.com/dreimer1986/ha_animated_backgrounds#config) describes all configuration options.

## <a name="screenshots"></a>Screenshots


**Kataware-doki**
<p align="center">
  <img src="https://raw.githubusercontent.com/dreimer1986/yourname_uix/refs/heads/master/assets/kataware-doki-home-overview.webp" alt="Kataware-doki - Home overview">
</p>

**Tiamat**
<p align="center">
  <img src="https://raw.githubusercontent.com/dreimer1986/yourname_uix/refs/heads/master/assets/tiamat-home-overview.webp" alt="Tiamat - Home overview">
</p>

**Original**
<p align="center">
  <img src="https://raw.githubusercontent.com/dreimer1986/yourname_uix/refs/heads/master/assets/original-home-overview.webp" alt="Original - Home overview">
</p>

**Kataware-doki - Settings - About**
<p align="center">
  <img src="https://raw.githubusercontent.com/dreimer1986/yourname_uix/refs/heads/master/assets/kataware-doki-settings-about.webp" alt="Kataware-doki - Settings - About">
</p>

**Tiamat - Settings - About**
<p align="center">
  <img src="https://raw.githubusercontent.com/dreimer1986/yourname_uix/refs/heads/master/assets/tiamat-settings-about.webp" alt="Tiamat - Settings - About">
</p>

**Original - Settings - About**
<p align="center">
  <img src="https://raw.githubusercontent.com/dreimer1986/yourname_uix/refs/heads/master/assets/original-settings-about.webp" alt="Original - Settings - About">
</p>

**Kataware-doki - Mobile**
<p align="center">
  <img src="https://raw.githubusercontent.com/dreimer1986/yourname_uix/refs/heads/master/assets/kataware-doki-mobile.webp" alt="Kataware-doki - Mobile version" width="50%">
</p>

**Tiamat - Mobile**
<p align="center">
  <img src="https://raw.githubusercontent.com/dreimer1986/yourname_uix/refs/heads/master/assets/tiamat-mobile.webp" alt="Tiamat - Mobile version" width="50%">
</p>

**Original - Mobile**
<p align="center">
  <img src="https://raw.githubusercontent.com/dreimer1986/yourname_uix/refs/heads/master/assets/original-mobile.webp" alt="Original - Mobile version" width="50%">
</p>

## Liquid Glass sidebar (module 0.5.0+)

All three theme variants enable individual glass navigation buttons with `liquid-glass-sidebar: "1"`. Install/update the combined HACS module from [ha_animated_backgrounds](https://github.com/dreimer1986/ha_animated_backgrounds), update the theme YAMLs and reload themes and the frontend. Load the module using the existing `frontend.extra_module_url` list to cover the sidebar on all HA pages.

Sidebar defaults: strength 54, bevel 24, blur 1.5, radius 22px. These use `liquid-glass-sidebar-strength`, `liquid-glass-sidebar-bevel`, `liquid-glass-sidebar-blur` and `liquid-glass-sidebar-radius`; background and shadow are independently configurable too. The ordinary card settings remain unchanged. UIX leaves active glass fills to the module and restores the original card fill when it is disabled. Set `liquid-glass-sidebar: "0"` to opt out.

The script/theme interaction was checked locally with all three UIX styles. The earlier glass module was confirmed working by the user in Android Chrome and the official HA app; the new sidebar still needs a device check.

The combined HACS module includes the startup/navigation improvements and Liquid Glass 0.6.0. Existing glass parameters need no changes.

## Releases

Pushes to `master` run the release workflow, create a version tag and publish a GitHub release with `yourname_uix-assets.zip` for supplemental static files. The workflow can also be started manually. HACS users receive theme updates through the release channel; installing from the default branch is a separate choice. To build the supplemental ZIP locally, run `python scripts/package_assets.py`.
