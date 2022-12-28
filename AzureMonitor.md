Azure Monitor
Azure Monitor is a service provided by Microsoft Azure that enables you to monitor the health and performance of your Azure resources. It provides data and actionable insights to monitor your applications, infrastructure, and network.

Azure Monitor is a service provided by Microsoft Azure that enables you to monitor the health and performance of your Azure resources. It provides data and actionable insights to monitor your applications, infrastructure, and network.

Azure Monitor Network Insights is a feature of Azure Monitor that helps you monitor and troubleshoot network performance issues in your Azure virtual network. It provides detailed visibility into network traffic flows, including information about latency, network errors, and network security. It also includes tools to help you diagnose and resolve network performance issues.

Azure Monitor Network Insights is useful for monitoring and troubleshooting network performance in Azure virtual networks, particularly in scenarios

Key points covered in the Quiz
The key components of Azure Monitor for Networks are: Network health and metrics, Connectivity, Traffic, Diagnostic Toolkit, and Application Insights.
Dependency view is currently available for Azure Application Gateway, Azure Virtual WAN, Azure Load Balancer, and Azure Traffic Manager.
To troubleshoot VPN connectivity, you can use the Diagnostic Toolkit or the Traffic tab in Azure Monitor for Networks.
Connection Monitor collects metrics using lightweight agents configured with the VMs or through the Azure monitor API.
To enable connection monitoring, NSG and firewall rules should allow packets over TCP or ICMP between the source and destination.
Connection Monitor tracks changes in reachability, latency, and throughput.
Destination endpoints that can be configured with Connection Monitor include Microsoft 365 URLs, Dynamics 365 URLs, custom URLs, Azure VM resource IDs, IPv4, IPv6, FQDN, any domain name, Azure AD URL, and Akamai URL.
Flow logs operate at layer 3 of the network.
Flow log collection can occur at a 1-minute or 5-minute interval.
Flow logs have a retention feature that allows them to be automatically deleted after 90 days of their creation.

Sample Powershell script
        
        # Install the Azure Resource Manager PowerShell module
        Install-Module -Name AzureRM

        # Connect to your Azure account
        Connect-AzureRMAccount

        # Select the Azure subscription you want to use
        Select-AzureRMSubscription -SubscriptionId <your-subscription-id>

        # Create a resource group for your Azure Monitor resources
        New-AzureRmResourceGroup -Name "MyResourceGroup" -Location "EastUS"

        # Create an Azure Monitor Network Insights resource
        New-AzureRmNetworkWatcher -Name "MyNetworkWatcher" -ResourceGroupName "MyResourceGroup" -Location "EastUS"

        # Enable Azure Monitor Network Insights for a virtual network
        Set-AzureRmNetworkWatcherConfig -NetworkWatcher "MyNetworkWatcher" -ResourceGroupName "MyResourceGroup" -Enabled $true

        # Monitor network traffic flows in your virtual network
        Get-AzureRmNetworkWatcherFlowLog -NetworkWatcher "MyNetworkWatcher" -ResourceGroupName "MyResourceGroup"

        # Diagnose and resolve network performance issues
        Troubleshoot-AzureRmNetworkWatcherConnection -NetworkWatcher "MyNetworkWatcher" -ResourceGroupName "MyResourceGroup" -Protocol TCP -LocalIPAddress "10.0.0.4" -RemoteIPAddress "10.0.0.5" -RemotePort 80
        
        
What does the code do?
This code installs the Azure Resource Manager PowerShell module, connects to your Azure account, selects the Azure subscription you want to use, creates a resource group and an Azure Monitor Network Insights resource, enables Azure Monitor Network Insights for a virtual network, monitors network traffic flows in the virtual network, and troubleshoots network performance issues.

You can use the Get-AzureRmNetworkWatcherFlowLog cmdlet to retrieve information about network traffic flows in your virtual network, and the Troubleshoot-AzureRmNetworkWatcherConnection cmdlet to diagnose and resolve network performance issues.

[Learn more about Azure Monitor Network Insights](https://learn.microsoft.com/en-us/azure/network-watcher/network-insights-overview)
