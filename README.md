# Your Name. - UIX & Animated Background Edition.
Home Assistant theme inspired by Makoto Shinkai's 2016 film 君の名は。

Two dark variants, both built around frosted glass cards, a blurred background, and a shared amber accent that ties them together.

**Kataware-doki** — named after the split-twilight moment in the film. Deep indigo backgrounds, lavender as the primary colour, comet amber for active states. Warm and atmospheric.

**Tiamat** — named after the comet itself. Same structure, but the lavender is replaced with electric blue against a deep navy sky. Colder, more precise, still unmistakably the same world.

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
1. Open the Community Store (HACS)
2. Search for `Your Name. UIX & Animated Background Edition`
3. Install it
4. Restart Home Assistant
5. Possible [Bug](#bug)

### <a name="manual_installation"></a>Manual installation
1. Create a folder `yourname_uix`  in your Home Assistant themes folder.
2. Copy the file `yourname_uix.yaml` into the identical named themes folder.
3. Restart Home Assistant

### <a name="activate_transparent_sidebar"></a>Activate transparent Sidebar and animated Background support
!! This section is needed regardless of the installation method used !!

**Get the files mentioned below from here: https://github.com/dreimer1986/ha_animated_backgrounds**

1. styles.js and videoBackground.css must be in `www/` folder
2. Go to the Dashboard Resources Settings
3. Add a new JavaScript-Module and type in: `/local/styles.js?v=1`
4. Open your `configuration.yaml`
5. Add `/local/styles.js?v=1` to the frontend section:
   <pre>
   frontend:
     themes: !include_dir_merge_named themes
     extra_module_url:
       - /local/styles.js?v=1
   </pre>
7. Follow the steps in here to configure the JavaScript-Module. https://github.com/dreimer1986/yourname_uix/blob/master/README-script.md

### <a name="activate_animations"></a>Activate animated Backgrounds
!! This section is needed regardless of the installation method used !!

I did not yet add animations in my repo, because I have no clue if that is legal, but you can do by yourself then.
Create the `animated_backgrounds` folder inside `www/` and copy the MP4 files you want to have as background in there.
Open your styles.js and be sure that under filesRandom all your filenames are in the list. Be 100% sure to keep the format. ['file1.mp4', 'file2.mp4', 'file3.mp4']

### <a name="enable_the_theme"></a>Enable the theme
- Open your **Profile** in Home Assistant and select either **Your Name. - Kataware-doki** or **Your Name. - Tiamat**.

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

- The needed JS Script file cannot be installed by HACS! These parts have to be done when using HACS or doing things manually, if you want the animated backgrounds.

- The JS Script has some nice other features, too. I tried to get the most important stuff from Villhelm's (RIP) Animated background working. More information and how to use it on your own themes will slowly grow up here: https://github.com/dreimer1986/yourname_uix/blob/master/README-script.md

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
