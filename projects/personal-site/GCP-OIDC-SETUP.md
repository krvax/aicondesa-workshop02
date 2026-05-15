# GCP Workload Identity Federation (WIF) Setup

This document outlines the steps taken to configure keyless authentication between GitHub Actions and Google Cloud Platform for the deployment of this repository's projects (like the Personal Site).

## Overview

Instead of using long-lived Service Account JSON keys (`IAM keys`), which pose security risks, we use **Workload Identity Federation (OIDC)**. This allows GitHub Actions workflows to request short-lived, auto-expiring access tokens directly from GCP.

## Configuration Details

*   **GCP Project ID**: `mx-coatl-aicondesa-workshop02`
*   **GCP Project Number**: `383578626035`
*   **GitHub Repository**: `krvax/AI-Club-Condesa-Workshops`
*   **Service Account**: `github-deploy@mx-coatl-aicondesa-workshop02.iam.gserviceaccount.com`
*   **Workload Identity Pool**: `github-pool`
*   **OIDC Provider**: `github-provider`

## Steps Executed

The following setup was successfully executed to link the repository:

1.  **Created Workload Identity Pool**:
    A pool named `github-pool` was created to manage external identities.
2.  **Created OIDC Provider**:
    A provider named `github-provider` was created, connected to the GitHub Actions issuer URL, and configured to map GitHub claims (`assertion.sub`, `assertion.repository`) to Google attributes.
3.  **Created Service Account**:
    Created the `github-deploy` Service Account, which acts as the identity in GCP.
4.  **Granted Necessary Roles**:
    The Service Account was granted the following roles to allow deployment to Cloud Run:
    *   `roles/run.admin` (Manage Cloud Run services)
    *   `roles/artifactregistry.writer` (Push containers)
    *   `roles/iam.serviceAccountUser` (Act as the service account for Cloud Run)
    *   `roles/cloudbuild.builds.editor` (Run Cloud Build via deploy command)
    *   `roles/storage.admin` (Manage source code storage for Cloud Build)
5.  **Bound WIF to Service Account**:
    Granted the `roles/iam.workloadIdentityUser` role to the specific GitHub repository (`krvax/AI-Club-Condesa-Workshops`) allowing it to impersonate the `github-deploy` Service Account.

## Using it in GitHub Actions

The authentication is utilized via the `google-github-actions/auth` step in your workflows:

```yaml
- name: Authenticate to Google Cloud
  uses: google-github-actions/auth@v2
  with:
    workload_identity_provider: 'projects/383578626035/locations/global/workloadIdentityPools/github-pool/providers/github-provider'
    service_account: 'github-deploy@mx-coatl-aicondesa-workshop02.iam.gserviceaccount.com'
```

No secrets are needed!
