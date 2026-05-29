---
source_url: https://openai.com/index/work-with-codex-from-anywhere/
ingested: 2026-05-29
ingested_by: agent-alpha
source_type: article
category: agent-engineering, codex
credibility_tier: primary
evidence_grade: medium
context: Historical Tolaria backfill item from 2026-05-18 Alpha session; inspect OpenAI Codex mobile/remote-work article and linked docs for Codex/Hermes workflow implications.
origin_session: /home/admin/.hermes/profiles/agent-alpha/sessions/session_20260518_035959_5d23a7.json
---

# Work with Codex from anywhere

Raw archival note for the OpenAI article and first-level linked OpenAI developer docs.

## Original request metadata

- URL: https://openai.com/index/work-with-codex-from-anywhere
- Source type: article
- Category: agent-engineering, codex
- Credibility tier supplied: unknown
- Evidence grade supplied: unknown
- First seen: 2026-05-18T03:59:59.654856
- Context preview: "Inspect the linked source https://openai.com/index/work-with-codex-from-anywhere/ and summarize what it is, the technical/product mechanism, why it matters for Codex/Hermes workflows, and whether it w"

## Fetch notes

- Direct urllib/browser access to the OpenAI article hit Cloudflare/bot-detection/403.
- The article and linked docs were fetched via Jina Reader snapshots for archival.
- Related links inspected:
  - https://developers.openai.com/codex/remote-connections — primary OpenAI docs for mobile/remote host connections, SSH hosts, host requirements, relay behavior, permissions, and troubleshooting.
  - https://developers.openai.com/codex/enterprise/access-tokens — primary OpenAI docs for workspace-scoped Codex access tokens for non-interactive automation.
  - https://developers.openai.com/codex/hooks — primary OpenAI docs for Codex lifecycle hooks, trust model, managed hooks, events, schemas, and examples.

## Initial source-check summary

- What it is: OpenAI product announcement for using Codex from the ChatGPT mobile app and across connected host machines, with linked docs on remote connections, access tokens, and hooks.
- Technical/product mechanism: Codex continues to run on a trusted host (Mac app, SSH host, devbox, or managed environment) while ChatGPT mobile sends prompts, approvals, and follow-ups through a secure relay. The host retains files, credentials, permissions, plugins, MCP servers, browser/computer-use setup, and local tools. OpenAI also documents workspace-scoped access tokens for non-interactive `codex exec` automation and hooks for lifecycle policy/validation/logging/memory behaviors.
- Why it matters for Codex/Hermes workflows: the source identifies reusable workflow primitives for long-running local agents: mobile attention/approval loops, host/device separation, remote devbox routing, workspace-governed automation identity, hooks for prompt/tool policy and validation, task-completion notifications, and diffs/test-output review from a remote device.
- Evidence notes: primary OpenAI docs, but still product-documentation evidence rather than independent benchmark data. Claims about adoption scale and productivity are not independently substantiated here. Durable Tolaria follow-up should focus on extracting workflow primitives, constraints, risks, and approval proposal options rather than assuming adoption.


---

## Archived fetch: codex_anywhere_0.md

```markdown
Title: Work with Codex from anywhere

URL Source: https://openai.com/index/work-with-codex-from-anywhere/

Markdown Content:
Codex is now in the ChatGPT mobile app so you can stay in the loop from anywhere while Codex gets work done across your laptops, devboxes, or remote environments.

As agents take on longer-running work, a new rhythm for collaboration is emerging. To keep work moving, you need to be able to easily answer a question, review what Codex found, change direction, approve what comes next, or add a new idea.

More than 4 million people now use Codex every week, and we’re seeing how much those small moments matter. A quick check-in can keep a thread moving, prevent unnecessary rework, or help Codex make progress with the right context. Now you can do that from your phone. Get started [here⁠(opens in a new window)](https://developers.openai.com/codex/remote-connections).

## Stay connected to active work from anywhere

Codex in the ChatGPT mobile app is a fully-featured mobile experience for getting work done with Codex. When you connect to any of your machines where Codex is running (whether that’s your laptop, a dedicated Mac mini, or a managed remote environment), the app loads the live state from that environment so you can work fluidly across active threads, approvals, plugins, and project context.

This is more than the ability to remotely control a single task or dispatch new tasks to your computer. From your phone, you can work across all of your threads, review outputs, approve commands, change models, or start something new. Your files, credentials, permissions, and local setup stay on the machine where Codex is operating, while updates flow back to your phone in real time, including screenshots, terminal output, diffs, test results, and approvals.

Under the hood, Codex uses a secure relay layer that keeps trusted machines reachable across devices without exposing them directly to the public internet. That relay also keeps active session state and context synced anywhere you’re signed in with ChatGPT.

## Step in when it matters

As Codex handles work over longer stretches, timely guidance becomes a bigger part of keeping that work useful. From your phone, you can start work when it is top of mind, unblock it when your judgment is needed, and stay close to the result as it takes shape.

With Codex in your pocket, now you can:

*   **Start investigating a bug while waiting for your coffee.** Because Codex is running from your development environment, it can begin inspecting the relevant files, reproduce the issue in the browser, run tests, and begin working toward a fix. If Codex needs clarification or permission to continue, you can answer or approve from your phone. And as it works, you can follow along with screenshots, terminal output, test results, and eventually review the resulting diff before you are back at your computer.
*   **Reach a decision point during your commute.** Before leaving for the office, you ask Codex to take on a refactor that will need time to work through, expecting to review the result when you get to your desk. Mid-commute, Codex finds two viable approaches and needs your direction before it can continue. From your phone, you review the tradeoffs, choose a path, and by the time you arrive, the task has kept moving in the direction you wanted.
*   **Head into a fast-moving customer conversation better prepared.** You come out of back-to-back meetings to find a support issue evolving across Slack, email, documents, and browser-based tools, with a customer call coming up next. From your phone, you ask Codex to synthesize the latest updates, flag the key open questions, and prepare a concise briefing for the conversation. If new details come in, you can ask Codex to refresh the summary before you join.
*   **Turn a new idea into forward motion while it is still fresh.** Whether you are at lunch, out for a walk, or listening to something that sparks a thought, you can send it to Codex from your phone by starting a new thread or adding it to active work. The task can begin taking shape before you return to your desk, without pulling you fully out of the moment that sparked it.

## Run Codex in enterprise environments

Many teams already develop inside managed remote environments that provide approved dependencies, credentials, security policies, and compute resources.

With Remote SSH now generally available, Codex can connect directly into those environments. The desktop app automatically detects hosts from your SSH configuration and lets you create projects and run threads inside remote machines just like you would locally.

Once connected, those environments can become accessible across your authorized ChatGPT devices through the same secure relay infrastructure. That means you can start work on your desktop, steer execution from your phone, and keep long-running tasks moving without staying tied to a single machine.

We’re also releasing several updates that expand how teams can automate, customize, and manage Codex at scale:

*   [**Programmatic access tokens**⁠(opens in a new window)](https://developers.openai.com/codex/enterprise/access-tokens) provide scoped credentials that can be issued directly from ChatGPT workspace settings for CI pipelines, release workflows, and internal automations.
*   [**Hooks**⁠(opens in a new window)](https://developers.openai.com/codex/hooks) are now generally available and can be used to scan prompts for secrets, run validators, log conversations, create memories, or customize Codex behavior for specific repositories and directories.
*   **Support for HIPAA-compliant use of Codex in local environments** (CLI, IDE, App) for ChatGPT Enterprise workspaces, enabling healthcare organizations to support patient care and operational workflows with greater speed and confidence.

## Availability

Codex in the ChatGPT mobile app is rolling out in preview on iOS and Android across all plans, including Free and Go, in all supported regions. Update the ChatGPT mobile app and the Codex app on macOS to try it out. Support for connecting your phone to the Codex app on Windows is coming soon.

Remote SSH and Hooks are available on all plans as well. Programmatic access tokens are available on Enterprise and Business plans. HIPAA-compliant use is supported for eligible ChatGPT Enterprise workspaces only when Codex is used in local environments.

```

---

## Archived fetch: codex_anywhere_1.md

```markdown
Title: Remote connections – Codex | OpenAI Developers

URL Source: https://developers.openai.com/codex/remote-connections

Published Time: Fri, 29 May 2026 08:40:54 GMT

Markdown Content:
Remote connections let you use Codex from another device or another machine. Use Codex in the ChatGPT mobile app to work with Codex on a connected Mac, continue work from another Codex App device, or connect the Codex App to projects on an SSH host.

Remote access uses the connected host’s projects, threads, files, credentials, permissions, plugins, Computer Use, browser setup, and local tools.

*   Start new threads in projects on the host, or continue existing ones.
*   Send follow-up instructions, answer questions, and steer active work.
*   Approve commands and other actions.
*   Review outputs, diffs, test results, terminal output, and screenshots.
*   Get notified when Codex completes a task or needs your attention.
*   Switch between connected hosts and threads.

The next sections cover using Codex in the ChatGPT mobile app to control a Codex App host. To connect Codex to a project on an SSH host, see [connect to an SSH host](https://developers.openai.com/codex/remote-connections#connect-to-an-ssh-host).

Codex mobile setup currently requires the Codex App for macOS. The Codex App for Windows does not support mobile setup yet.

Make sure you have:

*   Codex access in the ChatGPT account and workspace you want to use.
*   The latest ChatGPT mobile app on an iOS or Android device. If you do not see Codex in the ChatGPT mobile app, update ChatGPT first.
*   The latest Codex App for macOS running on a Mac host that is awake, online, and signed in to the same account and workspace. Mobile setup starts from the Codex App; you cannot set it up from the Codex CLI or IDE Extension.
*   Any required multi-factor authentication, SSO, or passkey configuration for that account or workspace.

If you use Codex through a ChatGPT workspace, your admin may need to enable Remote Control access before you can connect from your phone.

Start in the Codex App on the host you want to connect. The setup flow enables remote access for that host, then shows a QR code you can scan from your phone.

1.   Start Codex mobile setup.

Open Codex on the host and select **Set up Codex mobile** in the sidebar.

2.   Scan the QR code.

Use your phone to scan the QR code shown by Codex. The code opens ChatGPT so you can finish connecting the mobile app to the host.

3.   Finish setup in ChatGPT.

ChatGPT opens the Codex mobile setup flow. Confirm the same ChatGPT account and workspace, then complete any required multi-factor authentication, SSO, or passkey steps. After setup succeeds, the host appears in Codex on your phone.

4.   Review host settings.

In Codex on the host, use **Settings > Connections** to manage connected devices. You can also choose whether to keep the computer awake, enable Computer Use, or install the Chrome extension.

Start with the Mac laptop or desktop where you already use Codex. Add an always-on Mac or SSH host when you need continuous access or a different environment.

### Your Mac laptop or desktop

Connect the Mac where you already run Codex day to day. This gives remote access to the same projects, threads, credentials, plugins, and local setup you already use.

If that Mac sleeps, loses network access, or closes Codex, remote access stops until it is available again. If you use this computer as your host device, keep it plugged in and turn on **Keep this Mac awake** in the host’s connection settings.

On a Mac laptop, remote access can stay available with the lid open while the computer is plugged in. With the lid closed, connect an external display as well. Choosing **Sleep** still stops remote access.

### A dedicated always-on Mac

Use a dedicated always-on Mac when you want Codex to stay reachable for longer-running work.

Install the projects, credentials, plugins, MCP servers, and tools Codex should use on that machine.

### A remote development environment

Use an SSH host or managed devbox when the project already lives in a remote environment. Connect the Codex App host to that environment first; your phone still connects to the Codex App host, and Codex works in the remote environment with its dependencies, security policies, and compute resources.

For SSH setup details, see [connect to an SSH host](https://developers.openai.com/codex/remote-connections#connect-to-an-ssh-host).

For browser or desktop tasks on an always-on Mac or remote host, enable Computer Use and install the Chrome extension on that host.

Your phone sends prompts, approvals, and follow-up messages to Codex. The connected host provides the environment Codex uses.

That means:

*   Repository files and local documents come from the connected host.
*   Shell commands run on that host or remote environment.
*   Any plugin installed on that host is available when you use Codex remotely.
*   MCP servers, skills, browser access, and Computer Use come from that host’s configuration.
*   Signed-in websites and desktop apps are available only when the host can access them.
*   Sandboxing, security controls, and action approvals still apply to the connected session.

Codex uses a secure relay layer to keep trusted machines reachable across your authorized ChatGPT devices without exposing them directly to the public internet.

You can continue work from another signed-in Codex App device. For example, if your laptop is unavailable, you can start a thread from your phone on an always-on host, then later open Codex on your laptop and continue that same thread there.

In Codex on the laptop, use **Settings > Connections > Control other devices** to add the other host. A device can allow remote access and control another device at the same time.

In the Codex App, add remote projects from an SSH host and run threads against the remote filesystem and shell. Remote project threads run commands, read files, and write changes on the remote host.

Keep the remote host configured with the same security expectations you use for normal SSH access: trusted keys, least-privilege accounts, and no unauthenticated public listeners.

1.   Add the host to your SSH config so Codex can auto-discover it.

```
Host devbox
  HostName devbox.example.com
  User you
  IdentityFile ~/.ssh/id_ed25519
```

Codex reads concrete host aliases from `~/.ssh/config`, resolves them with OpenSSH, and ignores pattern-only hosts.

2.   Confirm you can SSH to the host from the machine running the Codex App.

`ssh devbox`
3.   Install and authenticate Codex on the remote host.

The app starts the remote Codex app server through SSH, using the remote user’s login shell. Make sure the `codex` command is available on the remote host’s `PATH` in that shell.

4.   In the Codex App, open **Settings > Connections**, add or enable the SSH host, then choose a remote project folder.

Remote connections use SSH to start and manage the remote Codex app server. Don’t expose app-server transports directly on a shared or public network.

If you need to reach a remote machine outside your current network, use a VPN or mesh networking tool instead of exposing the app server directly to the internet.

### You do not see the host on your phone

Confirm that the Codex App is running on the host, **Allow other devices to connect** is enabled, and the same ChatGPT account and workspace are selected on both devices.

### The approval request does not appear

Open Codex in the ChatGPT mobile app. Confirm that the phone and host use the same ChatGPT account and workspace, then scan the QR code again or restart setup from the host. If you use a ChatGPT workspace, ask your admin to confirm that Remote Control access is enabled.

### The remote session disconnects

Check whether the host went to sleep, lost network access, or closed Codex. Keep the host awake and connected while Codex works.

### Authentication blocks setup

Complete the account or workspace authentication prompt shown during setup. If your organization requires SSO, multi-factor authentication, or a passkey, finish that flow before trying again. If setup still fails, ask your workspace admin to confirm that Remote Control access is enabled.

*   [Codex App](https://developers.openai.com/codex/app)
*   [Codex App features](https://developers.openai.com/codex/app/features)
*   [Codex App settings](https://developers.openai.com/codex/app/settings)
*   [Computer Use](https://developers.openai.com/codex/app/computer-use)
*   [Chrome extension](https://developers.openai.com/codex/app/chrome-extension)
*   [Command line options](https://developers.openai.com/codex/cli/reference)
*   [Authentication](https://developers.openai.com/codex/auth)

```

---

## Archived fetch: codex_anywhere_2.md

```markdown
Title: Access tokens – Codex | OpenAI Developers

URL Source: https://developers.openai.com/codex/enterprise/access-tokens

Published Time: Fri, 29 May 2026 09:19:52 GMT

Markdown Content:
Codex access tokens let trusted automation run Codex local with a ChatGPT workspace identity. Use them when a script, scheduled job, or CI runner needs repeatable, non-interactive Codex access.

Codex access tokens are currently supported for ChatGPT Business and Enterprise workspaces.

Access tokens are created in the ChatGPT admin console at [Access tokens](https://chatgpt.com/admin/access-tokens). They are tied to the ChatGPT user and workspace that create them, and Codex uses them as agent identities for programmatic local workflows.

If a Platform API key works for your automation, keep using API key auth. Use Codex access tokens when the workflow specifically needs ChatGPT workspace access, ChatGPT-managed Codex entitlements, or enterprise workspace controls.

Use an access token when Codex needs to run without a user completing a browser sign-in. The token represents the ChatGPT workspace user who created it, so runs can use that user’s Codex access and appear in workspace governance data.

Codex checks the token when a run starts and ties the run to that workspace identity. Treat the token like any other automation secret: store it in a secret manager, keep it out of logs, and rotate it regularly.

Use access tokens for:

*   `codex exec` jobs that run from trusted automation.
*   Local scripts that need repeatable, non-interactive Codex runs.
*   Enterprise workflows where usage should be associated with a ChatGPT workspace user instead of an API organization key.

Main risks to avoid:

*   **Leaked secrets:** anyone with the token can start Codex runs as the token creator. Store tokens in a secret manager, keep them out of logs, and rotate them regularly.
*   **Untrusted runners:** public CI, forked pull requests, or shared machines can expose tokens to people outside your workspace. Use access tokens only on trusted runners.
*   **Shared identities:** one person’s token reused across unrelated teams makes ownership and audit trails harder to interpret. Create tokens for a specific workflow owner.
*   **Stale credentials:** long-lived tokens can remain active after the workflow changes. Prefer finite expirations and revoke tokens that are no longer used.
*   **Wrong credential type:** access tokens are for Codex local workflows. Use Platform API keys for general OpenAI API calls.

Use the Codex Local controls in workspace settings to turn on access token creation for allowed members.

1.   Go to [Workspace Settings > Settings and Permissions](https://chatgpt.com/admin/settings).
2.   In the Codex Local section, make sure **Allow members to use Codex Local** is turned on.
3.   Turn on **Allow members to use Codex access tokens** if all allowed members should be able to create access tokens.
4.   If you use custom roles for a narrower rollout, assign the access token permission only to groups that need to create tokens.

Keep access token creation limited to people or service owners who understand where the token will be stored, which automation will use it, and how it will be rotated.

Use the Access tokens page to name the token and choose when it expires.

1.   Go to [Access tokens](https://chatgpt.com/admin/access-tokens).
2.   Select **Create**.

1.   Enter a descriptive name, such as `release-ci` or `nightly-docs-check`.

1.   Choose an expiration. Prefer a finite expiration such as 7, 30, 60, or 90 days. If you choose **No expiration**, rotate the token on a regular schedule.
2.   Select **Create**.
3.   Copy the generated access token immediately. You cannot view it again after you close the modal.
4.   Store the token in your secret manager or CI secret store.

The shortest custom expiration is one day. Revoked and expired tokens cannot be used to start new Codex runs.

For ephemeral automation, store the token in `CODEX_ACCESS_TOKEN` and run Codex normally:

```
export CODEX_ACCESS_TOKEN="<access-token>"
codex exec --json "review this repository and summarize the top risks"
```

For a persistent local login, pipe the token to `codex login --with-access-token`:

```
printf '%s' "$CODEX_ACCESS_TOKEN" | codex login --with-access-token
codex exec "summarize the last release diff"
```

`codex login --with-access-token` stores an agent identity credential in Codex auth storage. If you prefer not to persist credentials on the machine, use the `CODEX_ACCESS_TOKEN` environment variable instead.

Rotate access tokens the same way you rotate other automation secrets:

1.   Create a replacement token.
2.   Update the secret in the runner, scheduler, or secret manager.
3.   Run a smoke test with the new token.
4.   Revoke the old token from [Access tokens](https://chatgpt.com/admin/access-tokens).

From the Access tokens page, workspace owners and admins can revoke any workspace token. Members with access token permission can revoke only the tokens they created.

Access token permissions are separate from the general Codex local permission. A member can have access to the Codex app, CLI, or IDE extension without being allowed to create access tokens.

| Capability | Workspace owners and admins | Member with access token permission | Member without access token permission |
| --- | --- | --- | --- |
| Open [Access tokens](https://chatgpt.com/admin/access-tokens) | Yes | Yes | No |
| Create access tokens | Yes, for their own ChatGPT workspace identity | Yes, for their own ChatGPT workspace identity | No |
| List access tokens | Workspace list, including who created each token | Only tokens they created | No |
| Revoke access tokens from the Access tokens page | Any token in the workspace | Only tokens they created | No page access |
| Grant or remove access token permission | Yes | No | No |
| Manage other Codex enterprise settings | Yes, based on admin role and Codex admin permissions | No, unless separately granted | No |

In short: workspace owners and admins manage access at the workspace level. Members need the access token permission to create and manage their own tokens, but the permission does not grant admin rights or access to other members’ tokens.

### The access tokens page returns 404 or forbidden

Ask a workspace owner or admin to confirm that Codex access tokens are enabled and that your role includes the access token permission.

### `codex login --with-access-token` fails

Confirm that you copied the generated access token, not a browser session token or Platform API key. Also confirm that the token has not expired or been revoked.

*   [Authentication](https://developers.openai.com/codex/auth)
*   [Non-interactive mode](https://developers.openai.com/codex/noninteractive)
*   [Admin setup](https://developers.openai.com/codex/enterprise/admin-setup)
*   [Governance](https://developers.openai.com/codex/enterprise/governance)

```

---

## Archived fetch: codex_anywhere_3.md

```markdown
Title: Hooks – Codex | OpenAI Developers

URL Source: https://developers.openai.com/codex/hooks

Published Time: Fri, 29 May 2026 06:28:52 GMT

Markdown Content:
Hooks are an extensibility framework for Codex. They allow you to inject your own scripts into the agentic loop, enabling features such as:

*   Send the conversation to a custom logging/analytics engine
*   Scan your team’s prompts to block accidentally pasting API keys
*   Summarize conversations to create persistent memories automatically
*   Run a custom validation check when a conversation turn stops, enforcing standards
*   Customize prompting when in a certain directory

Hooks are enabled by default. If you need to turn them off in `config.toml`, set:

```
[features]
hooks = false
```

Use `hooks` as the canonical feature key. `codex_hooks` still works as a deprecated alias.

Admins can force hooks off the same way in `requirements.toml` with `[features].hooks = false`.

Runtime behavior to keep in mind:

*   Matching hooks from multiple files all run.
*   Multiple matching command hooks for the same event are launched concurrently, so one hook cannot prevent another matching hook from starting.
*   Non-managed command hooks must be reviewed and trusted before they run.
*   `PreToolUse`, `PermissionRequest`, `PostToolUse`, `PreCompact`, `PostCompact`, `UserPromptSubmit`, `SubagentStop`, and `Stop` run at turn scope. `SessionStart` and `SubagentStart` run at thread or subagent-start scope.

Codex discovers hooks next to active config layers in either of these forms:

*   `hooks.json`
*   inline `[hooks]` tables inside `config.toml`

Installed plugins can also bundle lifecycle config through their plugin manifest or a default `hooks/hooks.json` file. See [Build plugins](https://developers.openai.com/codex/plugins/build#bundled-mcp-servers-and-lifecycle-config) for the plugin packaging rules.

In practice, the four most useful locations are:

*   `~/.codex/hooks.json`
*   `~/.codex/config.toml`
*   `<repo>/.codex/hooks.json`
*   `<repo>/.codex/config.toml`

If more than one hook source exists, Codex loads all matching hooks. Higher-precedence config layers don’t replace lower-precedence hooks. If a single layer contains both `hooks.json` and inline `[hooks]`, Codex merges them and warns at startup. Prefer one representation per layer.

Codex can also discover hooks bundled with enabled plugins. Plugin-bundled hooks load alongside other hook sources and use the same trust-review flow as other non-managed hooks.

Project-local hooks load only when the project `.codex/` layer is trusted. In untrusted projects, Codex still loads user and system hooks from their own active config layers.

Codex lists configured hooks before deciding which ones can run. Before a non-managed command hook can run, Codex requires you to review and trust the exact hook definition. Codex records trust against the hook’s current hash, so new or changed hooks are marked for review and skipped until trusted.

Use `/hooks` in the CLI to inspect hook sources, review new or changed hooks, trust hooks, or disable individual non-managed hooks. If hooks need review at startup, Codex prints a warning that tells you to open `/hooks`.

Managed hooks from system, MDM, cloud, or `requirements.toml` sources are marked as managed, trusted by policy, and can’t be disabled from the user hook browser.

For one-off automation that already vets hook sources outside Codex, pass `--dangerously-bypass-hook-trust` to run enabled hooks without requiring persisted hook trust for that invocation.

Hooks are organized in three levels:

*   A hook event such as `PreToolUse`, `PostToolUse`, `PreCompact`, `SubagentStart`, or `Stop`
*   A matcher group that decides when that event matches
*   One or more hook handlers that run when the matcher group matches

```
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup|resume",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.codex/hooks/session_start.py",
            "statusMessage": "Loading session notes"
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use_policy.py\"",
            "statusMessage": "Checking Bash command"
          }
        ]
      }
    ],
    "PermissionRequest": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/permission_request.py\"",
            "statusMessage": "Checking approval request"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/post_tool_use_review.py\"",
            "statusMessage": "Reviewing Bash output"
          }
        ]
      }
    ],
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/user_prompt_submit_data_flywheel.py\""
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/stop_continue.py\"",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

Notes:

*   `timeout` is in seconds.
*   If `timeout` is omitted, Codex uses `600` seconds.
*   `statusMessage` is optional.
*   `commandWindows` is an optional Windows-only command override. In TOML, use `command_windows` or `commandWindows`.
*   `async` is parsed, but async command hooks aren’t supported yet. Codex skips handlers with `async: true`.
*   Only `type: "command"` handlers run today. `prompt` and `agent` handlers are parsed but skipped.
*   Commands run with the session `cwd` as their working directory.
*   For repo-local hooks, prefer resolving from the git root instead of using a relative path such as `.codex/hooks/...`. Codex may be started from a subdirectory, and a git-root-based path keeps the hook location stable.

Equivalent inline TOML in `config.toml`:

```
[[hooks.PreToolUse]]
matcher = "^Bash$"

[[hooks.PreToolUse.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use_policy.py"'
timeout = 30
statusMessage = "Checking Bash command"

[[hooks.PostToolUse]]
matcher = "^Bash$"

[[hooks.PostToolUse.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/post_tool_use_review.py"'
timeout = 30
statusMessage = "Reviewing Bash output"
```

Enterprise-managed requirements can also define hooks inline under `[hooks]`. This is useful when admins want to enforce the hook configuration while delivering the actual scripts through MDM or another device-management system. To enforce managed hooks even for users who disabled hooks locally, pin `[features].hooks = true` in `requirements.toml` alongside `[hooks]`. To ignore user, project, session, and plugin hooks while still allowing administrator managed hooks, set `allow_managed_hooks_only = true`.

```
allow_managed_hooks_only = true

[features]
hooks = true

[hooks]
managed_dir = "/enterprise/hooks"
windows_managed_dir = 'C:\enterprise\hooks'

[[hooks.PreToolUse]]
matcher = "^Bash$"

[[hooks.PreToolUse.hooks]]
type = "command"
command = "python3 /enterprise/hooks/pre_tool_use_policy.py"
command_windows = 'py -3 C:\enterprise\hooks\pre_tool_use_policy.py'
timeout = 30
statusMessage = "Checking managed Bash command"
```

Notes for managed hooks:

*   `managed_dir` is used on macOS and Linux.
*   `windows_managed_dir` is used on Windows.
*   Codex doesn’t distribute the scripts in `managed_dir`; your enterprise tooling must install and update them separately.
*   Managed hook commands should use absolute script paths under the configured managed directory.
*   `allow_managed_hooks_only = true` skips hooks from user, project, session, and plugin sources, but still loads managed hooks from `requirements.toml` and other managed config layers.

When a plugin is enabled, Codex can load lifecycle hooks from that plugin alongside user, project, and managed hooks.

By default, Codex looks for `hooks/hooks.json` inside the plugin root. A plugin manifest can override that default with a `hooks` entry in `.codex-plugin/plugin.json`. The manifest entry can be a `./`-prefixed path, an array of `./`-prefixed paths, an inline hooks object, or an array of inline hooks objects.

```
{
  "name": "repo-policy",
  "hooks": "./hooks/hooks.json"
}
```

Manifest hook paths are resolved relative to the plugin root and must stay inside that root. If a manifest defines `hooks`, Codex uses those manifest entries instead of the default `hooks/hooks.json`.

Plugin hook commands receive these environment variables:

*   `PLUGIN_ROOT` is a Codex-specific extension that points to the installed plugin root.
*   `PLUGIN_DATA` is a Codex-specific extension that points to the plugin’s writable data directory.
*   Codex also sets `CLAUDE_PLUGIN_ROOT` and `CLAUDE_PLUGIN_DATA` for compatibility with existing plugin hooks.

Plugin hooks use the same event schema as other hooks. Installing or enabling a plugin doesn’t automatically trust its hooks; Codex skips plugin-bundled hooks until you review and trust the current hook definition.

The `matcher` field is a regex string that filters when hooks fire. Use `"*"`, `""`, or omit `matcher` entirely to match every occurrence of a supported event.

Only some current Codex events honor `matcher`:

| Event | What `matcher` filters | Notes |
| --- | --- | --- |
| `PermissionRequest` | tool name | Support includes `Bash`, `apply_patch`*, and MCP tool names |
| `PostToolUse` | tool name | Support includes `Bash`, `apply_patch`*, and MCP tool names |
| `PostCompact` | compaction trigger | Values are `manual` or `auto` |
| `PreCompact` | compaction trigger | Values are `manual` or `auto` |
| `PreToolUse` | tool name | Support includes `Bash`, `apply_patch`*, and MCP tool names |
| `SessionStart` | start source | Values are `startup`, `resume`, `clear`, and `compact` |
| `SubagentStart` | subagent type | Values depend on the subagent that starts |
| `SubagentStop` | subagent type | Values depend on the subagent that stops |
| `UserPromptSubmit` | not supported | Any configured `matcher` is ignored for this event |
| `Stop` | not supported | Any configured `matcher` is ignored for this event |

*For `apply_patch`, `matcher` values can also use `Edit` or `Write`.

Examples:

*   `Bash`
*   `^apply_patch$`
*   `Edit|Write`
*   `mcp__filesystem__read_file`
*   `mcp__filesystem__.*`
*   `startup|resume|clear|compact`
*   `manual|auto`

Every command hook receives one JSON object on `stdin`.

These are the shared fields you will usually use:

| Field | Type | Meaning |
| --- | --- | --- |
| `session_id` | `string` | Current Codex session id. Subagent hooks use the parent session id. |
| `transcript_path` | `string | null` | Path to the session transcript file, if any |
| `cwd` | `string` | Working directory for the session |
| `hook_event_name` | `string` | Current hook event name |
| `model` | `string` | Codex-specific extension. Active model slug |

Turn-scoped hooks list `turn_id` as a Codex-specific extension in their event-specific tables.

`SessionStart`, `PreToolUse`, `PermissionRequest`, `PostToolUse`, `UserPromptSubmit`, `SubagentStart`, `SubagentStop`, and `Stop` also include `permission_mode`, which describes the current permission mode as `default`, `acceptEdits`, `plan`, `dontAsk`, or `bypassPermissions`.

`transcript_path` points to a conversation transcript for convenience, but the transcript format is not a stable interface for hooks and may change over time.

If you need the full wire format, see [Schemas](https://developers.openai.com/codex/hooks#schemas).

`SessionStart`, `PreCompact`, `PostCompact`, `UserPromptSubmit`, `SubagentStop`, and `Stop` support these shared JSON fields. `SubagentStart` accepts the same shape for `systemMessage` and hook-specific context, but `continue: false` doesn’t stop the subagent:

```
{
  "continue": true,
  "stopReason": "optional",
  "systemMessage": "optional",
  "suppressOutput": false
}
```

| Field | Effect |
| --- | --- |
| `continue` | If `false`, marks that hook run as stopped |
| `stopReason` | Recorded as the reason for stopping |
| `systemMessage` | Surfaced as a warning in the UI or event stream |
| `suppressOutput` | Parsed today but not yet implemented |

Exit `0` with no output is treated as success and Codex continues.

`PreToolUse` and `PermissionRequest` support `systemMessage`, but `continue`, `stopReason`, and `suppressOutput` aren’t currently supported for those events. If a `PreToolUse` hook returns one of those unsupported fields, Codex marks that hook run as failed, reports the error, and continues the tool call.

`PostToolUse` supports `systemMessage`, `continue: false`, and `stopReason`. `suppressOutput` is parsed but not currently supported for that event.

### SessionStart

`matcher` is applied to `source` for this event.

Fields in addition to [Common input fields](https://developers.openai.com/codex/hooks#common-input-fields):

| Field | Type | Meaning |
| --- | --- | --- |
| `source` | `string` | How the session started: `startup`, `resume`, `clear`, or `compact` |

Plain text on `stdout` is added as extra developer context.

JSON on `stdout` supports [Common output fields](https://developers.openai.com/codex/hooks#common-output-fields) and this hook-specific shape:

```
{
  "hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": "Load the workspace conventions before editing."
  }
}
```

That `additionalContext` text is added as extra developer context.

### SubagentStart

`matcher` is applied to `agent_type` for this event.

Fields in addition to [Common input fields](https://developers.openai.com/codex/hooks#common-input-fields):

| Field | Type | Meaning |
| --- | --- | --- |
| `turn_id` | `string` | Codex-specific extension. Active Codex turn id |
| `agent_id` | `string` | Identifier for the subagent |
| `agent_type` | `string` | Subagent type or profile |
| `permission_mode` | `string` | Current permission mode |

Plain text on `stdout` is added as extra developer context for the subagent.

JSON on `stdout` supports `systemMessage` and this hook-specific shape:

```
{
  "hookSpecificOutput": {
    "hookEventName": "SubagentStart",
    "additionalContext": "Review the repository test conventions first."
  }
}
```

That `additionalContext` text is added as extra developer context for the subagent. `continue: false` is parsed for compatibility, but it doesn’t stop the subagent from starting.

### PreToolUse

`PreToolUse` can intercept Bash, file edits performed through `apply_patch`, and MCP tool calls. It’s still a guardrail rather than a complete enforcement boundary because Codex can often perform equivalent work through another supported tool path.

This doesn’t intercept all shell calls yet, only the simple ones. The newer `unified_exec` mechanism allows richer streaming stdin/stdout handling of shell, but interception is incomplete. Similarly, this doesn’t intercept `WebSearch` or other non-shell, non-MCP tool calls.

`matcher` is applied to `tool_name` and matcher aliases. For file edits through `apply_patch`, `matcher` values can use `apply_patch`, `Edit`, or `Write`; hook input still reports `tool_name: "apply_patch"`.

Fields in addition to [Common input fields](https://developers.openai.com/codex/hooks#common-input-fields):

| Field | Type | Meaning |
| --- | --- | --- |
| `turn_id` | `string` | Codex-specific extension. Active Codex turn id |
| `tool_name` | `string` | Canonical hook tool name, such as `Bash`, `apply_patch`, or an MCP name like `mcp__fs__read` |
| `tool_use_id` | `string` | Tool-call id for this invocation |
| `tool_input` | `JSON value` | Tool-specific input. `Bash` and `apply_patch` use `tool_input.command` while MCP tools send all arguments. |

Plain text on `stdout` is ignored.

JSON on `stdout` can use `systemMessage`. To deny a supported tool call, return this hook-specific shape:

```
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "Destructive command blocked by hook."
  }
}
```

Codex also accepts this older block shape:

```
{
  "decision": "block",
  "reason": "Destructive command blocked by hook."
}
```

You can also use exit code `2` and write the blocking reason to `stderr`.

To add model-visible context without blocking, return `hookSpecificOutput.additionalContext`:

```
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "additionalContext": "The pending command touches generated files."
  }
}
```

To rewrite a supported tool call without blocking, return `permissionDecision: "allow"` with `updatedInput`:

```
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow",
    "updatedInput": {
      "command": "echo rewritten"
    }
  }
}
```

For Bash commands and `apply_patch`, `updatedInput` must include a string `command` field. For MCP tools, `updatedInput` is the replacement arguments object. Return `updatedInput` only with `permissionDecision: "allow"`; other `updatedInput` shapes are reported as errors.

`permissionDecision: "ask"`, legacy `decision: "approve"`, `continue: false`, `stopReason`, and `suppressOutput` are parsed but not supported yet. Codex marks the hook run as failed, reports the error, and continues the tool call.

### PermissionRequest

`PermissionRequest` runs when Codex is about to ask for approval, such as a shell escalation or managed-network approval. It can allow the request, deny the request, or decline to decide and let the normal approval prompt continue. It doesn’t run for commands that don’t need approval.

`matcher` is applied to `tool_name` and matcher aliases. Current canonical values include `Bash`, `apply_patch`, and MCP tool names such as `mcp__server__tool`; `apply_patch` also matches `Edit` and `Write`.

Fields in addition to [Common input fields](https://developers.openai.com/codex/hooks#common-input-fields):

| Field | Type | Meaning |
| --- | --- | --- |
| `turn_id` | `string` | Codex-specific extension. Active Codex turn id |
| `tool_name` | `string` | Canonical hook tool name, such as `Bash`, `apply_patch`, or an MCP name like `mcp__fs__read` |
| `tool_input` | `JSON value` | Tool-specific input. `Bash` and `apply_patch` use `tool_input.command` while MCP tools send all the args. |
| `tool_input.description` | `string | null` | Human-readable approval reason, when Codex has one |

Plain text on `stdout` is ignored.

Some tool inputs may include a human-readable description, but don’t rely on a `tool_input.description` field for every tool.

To approve the request, return:

```
{
  "hookSpecificOutput": {
    "hookEventName": "PermissionRequest",
    "decision": {
      "behavior": "allow"
    }
  }
}
```

To deny the request, return:

```
{
  "hookSpecificOutput": {
    "hookEventName": "PermissionRequest",
    "decision": {
      "behavior": "deny",
      "message": "Blocked by repository policy."
    }
  }
}
```

If multiple matching hooks return decisions, any `deny` wins. Otherwise, an `allow` lets the request proceed without surfacing the approval prompt. If no matching hook decides, Codex uses the normal approval flow.

Don’t return `updatedInput`, `updatedPermissions`, or `interrupt` for `PermissionRequest`; those fields are reserved for future behavior and fail closed today.

### PostToolUse

`PostToolUse` runs after supported tools produce output, including Bash, `apply_patch`, and MCP tool calls. For Bash, it also runs after commands that exit with a non-zero status. It can’t undo side effects from the tool that already ran.

This doesn’t intercept all shell calls yet, only the simple ones. The newer `unified_exec` mechanism allows richer streaming stdin/stdout handling of shell, but interception is incomplete. Similarly, this doesn’t intercept `WebSearch` or other non-shell, non-MCP tool calls.

`matcher` is applied to `tool_name` and matcher aliases. For file edits through `apply_patch`, `matcher` values can use `apply_patch`, `Edit`, or `Write`; hook input still reports `tool_name: "apply_patch"`.

Fields in addition to [Common input fields](https://developers.openai.com/codex/hooks#common-input-fields):

| Field | Type | Meaning |
| --- | --- | --- |
| `turn_id` | `string` | Codex-specific extension. Active Codex turn id |
| `tool_name` | `string` | Canonical hook tool name, such as `Bash`, `apply_patch`, or an MCP name like `mcp__fs__read` |
| `tool_use_id` | `string` | Tool-call id for this invocation |
| `tool_input` | `JSON value` | Tool-specific input. `Bash` and `apply_patch` use `tool_input.command` while MCP tools send all arguments. |
| `tool_response` | `JSON value` | Tool-specific output. For MCP tools, this is the MCP call result. |

Plain text on `stdout` is ignored.

JSON on `stdout` can use `systemMessage` and this hook-specific shape:

```
{
  "decision": "block",
  "reason": "The Bash output needs review before continuing.",
  "hookSpecificOutput": {
    "hookEventName": "PostToolUse",
    "additionalContext": "The command updated generated files."
  }
}
```

That `additionalContext` text is added as extra developer context.

For this event, `decision: "block"` doesn’t undo the completed Bash command. Instead, Codex records the feedback, replaces the tool result with that feedback, and continues the model from the hook-provided message.

You can also use exit code `2` and write the feedback reason to `stderr`.

To stop normal processing of the original tool result after the command has already run, return `continue: false`. Codex will replace the tool result with your feedback or stop text and continue from there.

`updatedMCPToolOutput` and `suppressOutput` are parsed but not supported yet. Codex marks the hook run as failed, reports the error, and continues normal processing of the tool result.

### PreCompact

`PreCompact` runs before Codex compacts the conversation. `matcher` is applied to `trigger`, whose values are `manual` and `auto`.

Fields in addition to [Common input fields](https://developers.openai.com/codex/hooks#common-input-fields):

| Field | Type | Meaning |
| --- | --- | --- |
| `turn_id` | `string` | Codex-specific extension. Active Codex turn id |
| `trigger` | `string` | What triggered compaction: `manual` or `auto` |

Plain text on `stdout` is ignored.

JSON on `stdout` supports [Common output fields](https://developers.openai.com/codex/hooks#common-output-fields). If a matching `PreCompact` hook returns `continue: false`, Codex stops before compacting.

### PostCompact

`PostCompact` runs after Codex compacts the conversation. `matcher` is applied to `trigger`, whose values are `manual` and `auto`.

Fields in addition to [Common input fields](https://developers.openai.com/codex/hooks#common-input-fields):

| Field | Type | Meaning |
| --- | --- | --- |
| `turn_id` | `string` | Codex-specific extension. Active Codex turn id |
| `trigger` | `string` | What triggered compaction: `manual` or `auto` |

Plain text on `stdout` is ignored.

JSON on `stdout` supports [Common output fields](https://developers.openai.com/codex/hooks#common-output-fields). If a matching `PostCompact` hook returns `continue: false`, Codex stops after compacting.

### UserPromptSubmit

`matcher` isn’t currently used for this event.

Fields in addition to [Common input fields](https://developers.openai.com/codex/hooks#common-input-fields):

| Field | Type | Meaning |
| --- | --- | --- |
| `turn_id` | `string` | Codex-specific extension. Active Codex turn id |
| `prompt` | `string` | User prompt that’s about to be sent |

Plain text on `stdout` is added as extra developer context.

JSON on `stdout` supports [Common output fields](https://developers.openai.com/codex/hooks#common-output-fields) and this hook-specific shape:

```
{
  "hookSpecificOutput": {
    "hookEventName": "UserPromptSubmit",
    "additionalContext": "Ask for a clearer reproduction before editing files."
  }
}
```

That `additionalContext` text is added as extra developer context.

To block the prompt, return:

```
{
  "decision": "block",
  "reason": "Ask for confirmation before doing that."
}
```

You can also use exit code `2` and write the blocking reason to `stderr`.

### SubagentStop

`matcher` is applied to `agent_type` for this event.

Fields in addition to [Common input fields](https://developers.openai.com/codex/hooks#common-input-fields):

| Field | Type | Meaning |
| --- | --- | --- |
| `turn_id` | `string` | Codex-specific extension. Active Codex turn id |
| `agent_id` | `string` | Identifier for the subagent |
| `agent_type` | `string` | Subagent type or profile |
| `agent_transcript_path` | `string | null` | Path to the subagent transcript file, if any |
| `stop_hook_active` | `boolean` | Whether this subagent was already continued |
| `last_assistant_message` | `string | null` | Latest subagent assistant message, if available |

`SubagentStop` expects JSON on `stdout` when it exits `0`. Plain text output is invalid for this event.

JSON on `stdout` supports [Common output fields](https://developers.openai.com/codex/hooks#common-output-fields). To ask Codex to continue the subagent flow, return:

```
{
  "decision": "block",
  "reason": "Run one more focused pass inside the subagent."
}
```

You can also use exit code `2` and write the continuation reason to `stderr`.

If any matching `SubagentStop` hook returns `continue: false`, that takes precedence over continuation decisions from other matching `SubagentStop` hooks.

### Stop

`matcher` isn’t currently used for this event.

Fields in addition to [Common input fields](https://developers.openai.com/codex/hooks#common-input-fields):

| Field | Type | Meaning |
| --- | --- | --- |
| `turn_id` | `string` | Codex-specific extension. Active Codex turn id |
| `stop_hook_active` | `boolean` | Whether this turn was already continued by `Stop` |
| `last_assistant_message` | `string | null` | Latest assistant message text, if available |

`Stop` expects JSON on `stdout` when it exits `0`. Plain text output is invalid for this event.

JSON on `stdout` supports [Common output fields](https://developers.openai.com/codex/hooks#common-output-fields). To keep Codex going, return:

```
{
  "decision": "block",
  "reason": "Run one more pass over the failing tests."
}
```

You can also use exit code `2` and write the continuation reason to `stderr`.

For this event, `decision: "block"` doesn’t reject the turn. Instead, it tells Codex to continue and automatically creates a new continuation prompt that acts as a new user prompt, using your `reason` as that prompt text.

If any matching `Stop` hook returns `continue: false`, that takes precedence over continuation decisions from other matching `Stop` hooks.

The linked `main` branch schemas may include hook fields that are not in the current release. Use this page as the release behavior reference.

If you need the exact current wire format, see the generated schemas in the [Codex GitHub repository](https://github.com/openai/codex/tree/main/codex-rs/hooks/schema/generated).

```
