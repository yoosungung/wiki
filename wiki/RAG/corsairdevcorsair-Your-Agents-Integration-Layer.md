---
title: "corsairdevcorsair Your Agent's Integration Layer"
related_raw: ["[[raw/corsairdevcorsair Your Agent's Integration Layer.md]]"]
tags: ['#inbox']
type: "wiki"
status: "published"
last_updated: "2026-08-23"
updated: "2026-08-23"
---

# corsairdevcorsair Your Agent's Integration Layer

## Corsair: The Unified Integration Layer for Agents

⭐ the repo · [Website](https://corsair.dev/) · [Discord](https://discord.gg/uNgCP3mSzU) · [X](https://x.com/corsairdotdev)

Corsair is the unified integration layer for your agents. Connect your Corsair instance to your agent and immediately get access to every integration. Your agent never sees the credentials, and you control exactly what it can do.

corsair-slack.mp4<video src="https://private-user-images.githubusercontent.com/50637008/593602913-a5db555a-7688-447d-9777-33f3dddfb03d.mp4?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODY5NDc4MDMsIm5iZiI6MTc4Njk0NzUwMywicGF0aCI6Ii81MDYzNzAwOC81OTM2MDI5MTMtYTVkYjU1NWEtNzY4OC00NDdkLTk3NzctMzNmM2RkZGZiMDNkLm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA4MTclMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwODE3VDA2MTgyM1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTNhMWE5MDY2ODAyNzU4Zjg2ZGNkOTAwYmEyZGU1YzM5MTdiNmE1ZTE2YTU1MGQ2MTVkMWE1N2I0MjA5ZDQyZGUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT12aWRlbyUyRm1wNCJ9.XkKlL9DT11M99HEcL2cIxxXmS9tONACL8rHe72cahrs" controls="controls"></video>

---

## Why this exists

Agents are now capable of anything. It feels silly to do a routine task manually. But you do it anyways, because giving agents the keys to all your apps feels reckless. One misunderstood instruction and they're sending an email you'd never send.

Corsair allows you to safely integrate with any app. Connect the Corsair MCP to any agent and have built-in tool calls, permissions, and scoped auth.

---

## Example: Sending an Email

You're away from your computer, so you ask your agent to send an email:

```
Send Sarah the Q1 numbers from the Financials folder in Drive.
```

Using Corsair, your agent calls Google Drive and then Gmail. You have permissions set up so your agent can't send an email without you seeing. Corsair intercepts the Gmail call, sees it's a send action, and creates a permission request:

```
Agent: I've drafted the email. This action requires your approval before it sends.

  ⚠️ gmail: messages.post
     To: sarah@corsair.dev
     Subject: "Q1 Numbers"
     
     Hi Sarah, attached is the breakdown we discussed on the call.

     <file>
     
     Best,
     Claude

  Review and approve: https://somepubliclink.com/review/a8f2c1
  Link expires in 10 minutes.
```

You open the link. Why does it say "Best, Claude"? You deny the permission, scold Claude, and it sends you a new request.

---

## Permission modes

Each integration has its own mode. Set GitHub to strict and Slack to cautious based on how much you trust each surface.

- **open** — everything runs immediately
- **cautious** *(recommended)* — reads and writes run immediately; destructive actions require approval
- **strict** — reads run immediately; writes require approval; destructive actions are blocked
- **readonly** — reads only; all writes and destructive actions are blocked

You can also override individual endpoints within any mode. For example, set Slack to `open` but require approval before sending any message.

---

## Multi-tenancy

Corsair is built for production. Set `multiTenancy: true` and every tenant gets isolated credentials, isolated data storage, and isolated permissions handling. You can scope a request to a tenant id and Corsair ensures there is no cross-contamination.

```
import { github } from '@corsair-dev/github';
import { slack } from '@corsair-dev/slack';
import { createCorsair } from 'corsair/core';

const corsair = createCorsair({
  multiTenancy: true,
  plugins: [slack(), github()],
});

const client = corsair.withTenant('org-456');
await client.slack.api.messages.post({ channel: '#alerts', text: 'Deploy complete.' });
```

---

## Webhooks

Every plugin is shipped with typed, signature-verified webhook handlers. All webhooks point to a single endpoint. Set it and forget it.

```
import { processWebhook } from 'corsair';

app.post('/webhooks', async (req, res) => {
  const webhook = await processWebhook(corsair, req.headers, req.body)
  
  return res.json(webhook.response)
});
```

---

## FAQ

Where are credentials stored?

In an encrypted database using envelope encryption. A KEK you control encrypts per-tenant data keys, which encrypt the actual secrets. If you'd rather manage keys yourself, pass them directly and skip the key manager.

Does the agent ever see my API keys?

No. The agent sees method names and results. Credentials are resolved internally by Corsair at call time. The agent cannot read, log, or exfiltrate them.

What happens if I deny an approval request?

The action is discarded. Nothing is sent, created, or modified. Your agent can try again with corrected parameters and will send a new approval request.

Can I use Corsair with multiple tenants?

Yes. Set `multiTenancy: true` and each tenant gets isolated credentials, data storage, and permission evaluation. Endpoint discovery is available at the root and doesn't require a tenant.

Can I use Corsair alongside direct SDK calls?

Yes. Corsair is a library. Use it where the permission layer and key management help, and drop down to individual SDKs when you need custom logic.

Can the agent go around the permission request? No. Corsair creates a permission request in a database the agent doesn't have access to. Your agent cannot get past the permission request until that database row is set to \`approved\`. What integrations do you currently support? For the full list of integrations, see our \[docs\]([https://docs.corsair.dev/guides/plugins](https://docs.corsair.dev/guides/plugins)). We're adding integrations regularly. If there's an integration you need, create a Github issue.

---

## License

Licensed under the Apache License, Version 2.0. See [LICENSE](https://github.com/corsairdev/corsair/blob/main/LICENSE) for details.

---

[

![Star History Chart](https://camo.githubusercontent.com/e8190ff5542d95bb3e998833dd3b944ca36e99aa236c539823f1471823bdc46c/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f63686172743f7265706f733d636f72736169726465762f636f727361697226747970653d64617465266c6567656e643d746f702d6c656674267365616c65645f746f6b656e3d316c747a6e433670684b432d66765437444c3730365a33743469653048566f635f355451386868477a6d6d7656314850674d5a3436464537794754475972353961414930724564314d55454d503633426a61565f74474c6c783669574d336f6b75747577334d49754435776a51306f785f7354553759624d6e4165466559334f4e736b73516a386b432d745630592d31666c4647327837595849535a737157654968527446356145435269556f696c51416958767747485a5441626a)

](https://www.star-history.com/?repos=corsairdev%2Fcorsair&type=date&legend=top-left)

---
- **Source:** Unknown
